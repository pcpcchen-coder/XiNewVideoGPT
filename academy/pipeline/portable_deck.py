#!/usr/bin/env python3
"""Edit the tracked PPTX at OOXML level; render the final deck with LibreOffice.

No ChatGPT package dependency. Retains reference shapes, run styles and images.
Changing paragraph counts requires an explicitly authored alternative layout.
"""
from pathlib import Path
import argparse
import zipfile
from lxml import etree as ET
import academy

NS = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
      'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}
def tag(prefix, local): return '{%s}%s' % (NS[prefix], local)
def text_of(body):
    return '\n'.join(''.join(p.itertext(tag('a', 't'))) for p in body.findall('a:p', NS))

def replace_body(body, value):
    paragraphs = body.findall('a:p', NS)
    lines = value.split('\n')
    if len(paragraphs) != len(lines):
        raise ValueError('Replacement must preserve paragraph count: ' + value)
    for paragraph, line in zip(paragraphs, lines):
        runs = paragraph.findall('a:r', NS)
        if not runs:
            run = ET.SubElement(paragraph, tag('a', 'r'))
            ET.SubElement(run, tag('a', 't')).text = line
        else:
            # Textboxes in the reference use homogeneous styles within each paragraph.
            # Keep the first run style, remove stale text from subsequent runs.
            runs[0].find('a:t', NS).text = line
            for run in runs[1:]:
                paragraph.remove(run)
        for br in paragraph.findall('a:br', NS): paragraph.remove(br)

def build(ep, render=True):
    academy.validate_episode(ep)
    m = academy.read(ep/'production/manifest.json')
    edits = academy.read(ep/'production/template-text.json')
    narration = academy.read(ep/'production/narration.json')
    source = academy.ROOT / m['templateEpisode'] / 'production/presentation'
    source = source / (Path(m['templateEpisode']).name + '.pptx')
    targets = {(e['slide'], e['old']): e['new'] for e in edits}
    if any(targets[(e['slide'], e['old'])] != e['new'] for e in edits):
        raise ValueError('Conflicting duplicate text mapping')
    seen = set()
    with zipfile.ZipFile(source) as z:
        blobs = {name:z.read(name) for name in z.namelist()}
    for i in range(1, 13):
        name = f'ppt/slides/slide{i}.xml'
        xml = ET.fromstring(blobs[name])
        for body in xml.findall('.//p:sp/p:txBody', NS):
            old = text_of(body)
            key = (i, old)
            if key in targets:
                value = targets[key]; seen.add(key)
            elif old == '父子科技學院  ·  FIRST WORKSTATION': value = m.get('seriesHeader', '父子科技學院')
            elif old.startswith('L001 · '): value = old.replace('L001', m['episode'], 1)
            elif old == '把 MacBook 變成我的工作站': value = m['title']
            else: continue
            replace_body(body, value)
        blobs[name] = ET.tostring(xml, xml_declaration=True, encoding='UTF-8', standalone=True)
        name = f'ppt/notesSlides/notesSlide{i}.xml'
        xml = ET.fromstring(blobs[name])
        body = None
        for shape in xml.findall('.//p:sp', NS):
            ph = shape.find('p:nvSpPr/p:nvPr/p:ph', NS)
            if ph is not None and ph.get('type') == 'body': body = shape.find('p:txBody', NS)
        if body is None: raise ValueError('Reference notes body missing')
        for p in body.findall('a:p', NS): body.remove(p)
        lines = [x['text'] for x in narration[i-1]['sentences']] + ['[Sources]'] + narration[i-1]['sources']
        for line in lines:
            p = ET.SubElement(body, tag('a', 'p')); r = ET.SubElement(p, tag('a', 'r'))
            ET.SubElement(r, tag('a', 't')).text = line
        blobs[name] = ET.tostring(xml, xml_declaration=True, encoding='UTF-8', standalone=True)
    if seen != set(targets): raise ValueError('Unmatched template mappings: ' + repr(set(targets)-seen))
    output = ep/'production/presentation'/f'{ep.name}.pptx'
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as z:
        for name, data in blobs.items(): z.writestr(name, data)
    # Parse every XML part in the actual final package, and verify final visible text.
    with zipfile.ZipFile(output) as z:
        for name in z.namelist():
            if name.endswith('.xml'): ET.fromstring(z.read(name))
        for i in range(1,13):
            xml = ET.fromstring(z.read(f'ppt/slides/slide{i}.xml'))
            texts = [text_of(b) for b in xml.findall('.//p:sp/p:txBody', NS)]
            for (slide, old), new in targets.items():
                if slide == i and new not in texts: raise ValueError('Final replacement not found')
    if render: academy.export_slides(ep)
    academy.write(ep/'qc/presentation-validation.json', {
        'renderer':'ooxml-template + LibreOffice', 'referenceSha256':academy.sha(source),
        'pptxSha256':academy.sha(output), 'slideCount':12, 'matchedMappings':len(seen),
        'xmlParsed':True, 'rendered':render, 'visualReview':'required; not established by structural checks'})
    return output

if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--episode', required=True)
    args=p.parse_args(); print(build((academy.ROOT/args.episode).resolve()))
