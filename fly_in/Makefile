install:
		pip install -r requirements.txt

run:
		python3

debug:
		python3 -m pdb

clean:
		find . -type d -name "__pycache__" -exec rm -r {} +
		rm -rf .mypy_cache

lint:
		python3 -m flake8 .
		python3 -m mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
		python3 -m flake8 .
		python3 -m mypy . --strict

.PHONY: install run debug clean lint lint-strict
