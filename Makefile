PYTHON ?= python3
NODE ?= node
EPISODE ?= episodes/season-01/ep02-binary-data

.PHONY: install tts tts-offline tts-f music render assemble verify all

install:
	npm install
	$(PYTHON) -m pip install -r requirements.txt

tts:
	$(PYTHON) pipeline/scripts/synthesize_edge_narration.py $(EPISODE)

tts-offline:
	$(NODE) pipeline/scripts/synthesize_narration.cjs $(EPISODE)

tts-f:
	$(NODE) pipeline/scripts/synthesize_elevenlabs_narration.cjs $(EPISODE)

music:
	$(PYTHON) pipeline/scripts/generate_music.py --episode $(EPISODE)

render:
	$(PYTHON) pipeline/scripts/render_episode.py --episode $(EPISODE)

assemble: render
	$(PYTHON) pipeline/scripts/assemble_episode.py --episode $(EPISODE)

verify:
	$(PYTHON) pipeline/scripts/verify_episode.py --episode $(EPISODE)

all: tts music assemble verify
