PYTHON ?= python3
NODE ?= node
EPISODE ?= episodes/season-01/ep01-computer-inside

.PHONY: install tts music render assemble verify all

install:
	npm install
	$(PYTHON) -m pip install -r requirements.txt

tts:
	$(NODE) pipeline/scripts/synthesize_narration.cjs $(EPISODE)

music:
	$(PYTHON) pipeline/scripts/generate_music.py --episode $(EPISODE)

render:
	$(PYTHON) pipeline/scripts/render_episode.py --episode $(EPISODE)

assemble: render
	$(PYTHON) pipeline/scripts/assemble_episode.py --episode $(EPISODE)

verify:
	$(PYTHON) pipeline/scripts/verify_episode.py --episode $(EPISODE)

all: tts music assemble verify
