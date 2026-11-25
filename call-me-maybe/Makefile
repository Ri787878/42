PYTHON_FILES = src
INSTALL_STAMP = .install_compiled

# Store caches and temporary files on sgoinfre (if the pc doesnt hav enough space aka 42 pcs)
CACHE_ROOT ?= $(HOME)/sgoinfre

export UV_CACHE_DIR := $(CACHE_ROOT)/uv-cache
export UV_PROJECT_ENVIRONMENT ?= $(CACHE_ROOT)/call-me-maybe-venv
export TMPDIR := $(CACHE_ROOT)/tmp
export HF_HOME := $(CACHE_ROOT)/huggingface

install: $(INSTALL_STAMP)
$(INSTALL_STAMP): Makefile pyproject.toml uv.lock
	mkdir -p "$(UV_CACHE_DIR)" "$(UV_PROJECT_ENVIRONMENT)" "$(TMPDIR)" "$(HF_HOME)"
	uv sync
	touch $(INSTALL_STAMP)

run: install
	uv run python -m src

debug: install
	uv run python -m pdb -m src

clean:
	find . -type d -name "__pycache__" -prune -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf .mypy_cache .pytest_cache
	rm -rf data/output
	rm -f $(INSTALL_STAMP)

fclean: clean
	rm -rf .venv 2>/dev/null || true

lint: install
	uv run flake8 $(PYTHON_FILES)
	uv run mypy $(PYTHON_FILES) \
		--warn-return-any --warn-unused-ignores --ignore-missing-imports \
		--disallow-untyped-defs --check-untyped-defs

lint-strict: install
	uv run flake8 $(PYTHON_FILES)
	uv run mypy --strict $(PYTHON_FILES)

.PHONY: install run debug clean fclean lint lint-strict