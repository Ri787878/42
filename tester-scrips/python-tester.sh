#!/usr/bin/env bash

set -u

TARGET_DIR="${1:-.}"

clear

echo "Python tester"
echo "Target directory: ${TARGET_DIR}"
echo "Commands:"
echo "  autopep8 --diff --exit-code <file>"
echo "  mypy <file>"
echo

if ! command -v autopep8 >/dev/null 2>&1; then
  echo "Error: autopep8 is not available in PATH."
  exit 127
fi

if ! command -v mypy >/dev/null 2>&1; then
  echo "Error: mypy is not available in PATH."
  exit 127
fi

if [[ ! -d "${TARGET_DIR}" ]]; then
  echo "Error: '${TARGET_DIR}' is not a directory."
  exit 1
fi

exit_code=0
found_files=0

while IFS= read -r -d '' file; do
  found_files=1
  echo "========================================"
  echo "File: ${file}"

  echo "[autopep8]"
  autopep8 --diff --exit-code "${file}"
  autopep8_exit=$?

  echo "[mypy]"
  mypy "${file}"
  mypy_exit=$?

  if [[ ${autopep8_exit} -eq 0 && ${mypy_exit} -eq 0 ]]; then
    echo "Status: OK (autopep8=0, mypy=0)"
  else
    echo "Status: Issues found (autopep8=${autopep8_exit}, mypy=${mypy_exit})"
  fi

  if [[ ${autopep8_exit} -ne 0 || ${mypy_exit} -ne 0 ]]; then
    exit_code=1
  fi

  echo

done < <(find "${TARGET_DIR}" -type f -name '*.py' -print0 | sort -z)

if [[ ${found_files} -eq 0 ]]; then
  echo "No Python files found."
fi

echo "Finished with exit code: ${exit_code}"
if [[ ${exit_code} -eq 0 ]]; then
  echo "Status: PASS"
else
  echo "Status: FAIL"
fi

exit "${exit_code}"
