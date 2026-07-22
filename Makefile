PYTHON ?= python3
EPISODE ?= episodes/season-01/ep01-computer-inside

.PHONY: render assemble verify all

render:
	$(PYTHON) pipeline/scripts/render_episode.py --episode $(EPISODE)

assemble: render
	$(PYTHON) pipeline/scripts/assemble_episode.py --episode $(EPISODE)

verify:
	$(PYTHON) pipeline/scripts/verify_episode.py --episode $(EPISODE)

all: assemble verify

