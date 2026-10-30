# SGOINFRE := $(shell [ -d /sgoinfre/$(USER) ] && echo /sgoinfre/$(USER) || echo $(HOME))
install:
	uv venv
	uv pip install -r requirements.txt

run:
	uv run call-me-maybe

debug:
	uv run python -m pdb src/call_me_maybe/__main__.py

clean:
	find . -type d -name ".mypy_cache" -exec rm -r {} +
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name "output" -exec rm -r {} +

lint:
	uv run python -m flake8 . --exclude=.venv
	uv run python -m mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	uv run python -m flake8 . --exclude=.venv
	uv run python -m mypy . --strict

.PHONY: install run debug clean lint lint-strict
