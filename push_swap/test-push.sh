#!/bin/bash

set -u

TMP_OUT="/tmp/push_swap_test_stdout"
TMP_ERR="/tmp/push_swap_test_stderr"
TMP_EXP="/tmp/push_swap_test_expected"
TMP_ACT_NORM="/tmp/push_swap_test_actual_norm"
TMP_EXP_NORM="/tmp/push_swap_test_expected_norm"
COLOR_RESET="\033[0m"
COLOR_PASS="\033[38;5;46m"
COLOR_FAIL="\033[38;5;160m"
TOTAL_TESTS=0
FAILED_TESTS=0

print_status()
{
    label="$1"
    passed="$2"

    if [ "$passed" -eq 1 ]
    then
        echo -e "$label: ${COLOR_PASS}Passed${COLOR_RESET}"
    else
        echo -e "$label: ${COLOR_FAIL}Failed${COLOR_RESET}"
    fi
}

normalize_file()
{
    infile="$1"
    outfile="$2"
    sed 's/[[:blank:]][[:blank:]]*/ /g; s/[[:space:]]*$//' "$infile" > "$outfile"
}

run_output_case()
{
    label="$1"
    expected_code="$2"
    expected_output="$3"
    shift 3

    "$@" >"$TMP_OUT" 2>"$TMP_ERR"
    actual_code=$?
    TOTAL_TESTS=$((TOTAL_TESTS + 1))
    case_failed=0

    printf "%s\n" "$expected_output" > "$TMP_EXP"
    normalize_file "$TMP_OUT" "$TMP_ACT_NORM"
    normalize_file "$TMP_EXP" "$TMP_EXP_NORM"

    echo "----------------------------------------"
    echo "Test: $label"

    if [ "$actual_code" -eq "$expected_code" ]
    then
        print_status "Program status" 1
    else
        print_status "Program status" 0
        case_failed=1
    fi

    exp_cmp=$(cat "$TMP_EXP_NORM")
    act_cmp=$(cat "$TMP_ACT_NORM")
    if [ "$act_cmp" = "$exp_cmp" ]
    then
        print_status "Output compare" 1
    else
        print_status "Output compare" 0
        case_failed=1
    fi

    if [ -s "$TMP_ERR" ]
    then
        print_status "Standard error empty" 0
        case_failed=1
    else
        print_status "Standard error empty" 1
    fi

    if [ "$case_failed" -eq 1 ]
    then
        FAILED_TESTS=$((FAILED_TESTS + 1))
    fi

    echo "Command: $*"
    echo "Expected return code: $expected_code"
    echo "Actual return code: $actual_code"
    echo "Expected output:"
    cat "$TMP_EXP"
    echo "Actual output:"
    cat "$TMP_OUT"

    if [ -s "$TMP_ERR" ]
    then
        echo "Standard error:"
        cat "$TMP_ERR"
        printf "\n"
    else
        echo "Standard error: <empty>"
    fi

    if [ "$case_failed" -eq 1 ]
    then
        echo "Diff (normalized):"
        diff -u <(cat "$TMP_EXP_NORM"; echo) <(cat "$TMP_ACT_NORM"; echo) || true
    fi
}

echo -e "\n[1/3] Building archive\n"
if ! make re
then
    echo "Build failed"
    exit 1
fi

echo -e "\n[2/3] Linking test binaries\n"
if ! cc -Wall -Wextra -Werror push_swap.a -o test
then
    echo "Link failed"
    exit 1
fi
if ! cp push_swap.a push_swap_nomain.a
then
    echo "Copy archive failed"
    exit 1
fi
if ! ar d push_swap_nomain.a main.o >/dev/null 2>&1
then
    echo "Removing main.o from archive failed"
    rm -f push_swap_nomain.a
    exit 1
fi
if ! cc -Wall -Wextra -Werror test.c push_swap_nomain.a -o test_moves
then
    echo "Link move tests failed"
    rm -f push_swap_nomain.a
    exit 1
fi
rm -f push_swap_nomain.a

echo -e "\n[3/3] Running output comparison tests\n"
run_output_case "Main output with quoted input" 0 "$(cat <<'EOT'
stack A: 3 -5 1 7 -2 -8 4 -1 6 -6 0 5 -3 2 -7 -4
stack B:
pb
stack A: -5 1 7 -2 -8 4 -1 6 -6 0 5 -3 2 -7 -4
stack B: 3
EOT
)" ./test "3 -5 1 7 -2 -8 4 -1 6 -6 0 5 -3 2 -7 -4"

run_output_case "Simple move demo output" 0 "$(cat <<'EOT'
stack A: 3 -5 1 7 -2 -8 4 -1 6 -6 0 5 -3 2 -7 -4
stack B:
pb
stack A: -5 1 7 -2 -8 4 -1 6 -6 0 5 -3 2 -7 -4
stack B: 3
=== move demo ===
stack A: 1 2 3
stack B: 4 5 6
sa
sb
ss
pb
pa
stack A: 1 2 3
stack B: 4 5 6
EOT
)" ./test_moves

echo "----------------------------------------"
echo "Total tests: $TOTAL_TESTS"
echo "Failed tests: $FAILED_TESTS"
echo "Passed tests: $((TOTAL_TESTS - FAILED_TESTS))"

rm -f test_moves test "$TMP_OUT" "$TMP_ERR" "$TMP_EXP" "$TMP_ACT_NORM" "$TMP_EXP_NORM"

if [ "$FAILED_TESTS" -eq 0 ]
then
    echo -e "Overall result: ${COLOR_PASS}Passed${COLOR_RESET}"
    exit 0
fi

echo -e "Overall result: ${COLOR_FAIL}Failed${COLOR_RESET}"
exit 1
