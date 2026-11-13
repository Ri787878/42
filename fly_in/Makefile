PYTHON_FILES = fly_in.py classes build visualizers
install: .install_compiled maps

.install_compiled:
	python3 -m venv fly-in
	fly-in/bin/pip install --upgrade pip
	fly-in/bin/pip install -r requirements.txt
	touch .install_compiled

maps:
	if [ -f maps.tar.gz ]; then \
		tar -xf maps.tar.gz; \
	elif [ -d maps ]; then \
		printf '%s\n' "Using existing maps directory"; \
	else \
		printf '%s\n' "[ERROR] Neither maps/ nor maps.tar.gz exists." >&2; \
		exit 1; \
	fi

run: install
	./fly-in/bin/python3 fly_in.py

debug:
	./fly-in/bin/python3 -m pdb fly_in.py

clean:
	find . -type d -name "__pycache__" -exec rm -r {} +
	rm -rf .mypy_cache
	rm -rf maps
	rm -f .install_compiled

fclean:
	rm -rf fly-in

lint:
	python3 -m flake8 $(PYTHON_FILES)
	python3 -m mypy $(PYTHON_FILES) \
		--warn-return-any --warn-unused-ignores --ignore-missing-imports \
		--disallow-untyped-defs --check-untyped-defs

lint-strict:
	python3 -m flake8 $(PYTHON_FILES)
	python3 -m mypy --strict $(PYTHON_FILES)

.PHONY: run debug clean fclean lint lint-strict install