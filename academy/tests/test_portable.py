"""Acceptance tests for the portable handoff; no TTS network or real L004 mutation."""
import sys
import shutil
import tempfile
import unittest
from unittest.mock import patch
import zipfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'pipeline'))
import academy as a
import portable_deck as deck

class PortableTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.ep=Path(self.tmp.name)/'l004-portable-test'
        shutil.copytree(ROOT/'episodes/academy/l003-keyboard-ninja/production',self.ep/'production')
        m=a.read(self.ep/'production/manifest.json'); m.update(episode='L004',deckRenderer='ooxml-template',title='測試用可編輯投影片')
        a.write(self.ep/'production/manifest.json',m)
    def tearDown(self): self.tmp.cleanup()
    def test_template_edit_preserves_images_and_adds_current_notes(self):
        output=deck.build(self.ep,render=False)
        template=ROOT/'episodes/academy/l001-mac-workstation/production/presentation/l001-mac-workstation.pptx'
        with zipfile.ZipFile(output) as actual, zipfile.ZipFile(template) as source:
            media=[n for n in source.namelist() if n.startswith('ppt/media/')]
            self.assertTrue(media)
            for name in media: self.assertEqual(actual.read(name),source.read(name))
        from pptx import Presentation
        p=Presentation(output)
        self.assertEqual(len(p.slides),12)
        alltext='\n'.join(sh.text for s in p.slides for sh in s.shapes if sh.has_text_frame)
        self.assertNotIn('L001',alltext)
        self.assertIn('L004',alltext)
        self.assertIn(a.read(self.ep/'production/narration.json')[0]['sentences'][0]['text'],p.slides[0].notes_slide.notes_text_frame.text)
    def test_unmatched_mapping_rejected(self):
        edits=a.read(self.ep/'production/template-text.json'); edits[0]['old']='不存在的舊文字'
        a.write(self.ep/'production/template-text.json',edits)
        with self.assertRaisesRegex(ValueError,'Unmatched'): deck.build(self.ep,render=False)
    def test_paragraph_change_rejected(self):
        edits=a.read(self.ep/'production/template-text.json'); edits[0]['new']='一\n二\n三'
        a.write(self.ep/'production/template-text.json',edits)
        with self.assertRaisesRegex(ValueError,'paragraph count'): deck.build(self.ep,render=False)
    def test_portable_placeholder_cannot_bypass_validation(self):
        edits=a.read(self.ep/'production/template-text.json'); edits[0]['new']='待編寫'
        a.write(self.ep/'production/template-text.json',edits)
        with self.assertRaisesRegex(ValueError,'placeholders'): a.validate_episode(self.ep)
    def test_package_rejects_missing_delivery_even_with_technical_pass(self):
        (self.ep/'qc').mkdir(exist_ok=True)
        a.write(self.ep/'qc/report.json',{'checks':[{'status':'PASS'}]})
        a.write(self.ep/'qc/verified-inputs.json',a.fingerprint(self.ep))
        dest=Path(self.tmp.name)/'delivery'
        with patch.object(a,'media_check'), self.assertRaisesRegex(ValueError,'Incomplete delivery'):
            a.package(self.ep,dest)
        self.assertFalse(dest.exists())
    def test_classroom_change_invalidates_verified_fingerprint(self):
        f=self.ep/'classroom/task.md';f.parent.mkdir();f.write_text('v1')
        old=a.fingerprint(self.ep);f.write_text('v2')
        self.assertNotEqual(old,a.fingerprint(self.ep))
if __name__=='__main__': unittest.main()
