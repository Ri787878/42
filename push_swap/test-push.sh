#!/bin/bash

set -u

TMP_OUT="/tmp/push_swap_test_stdout"
TMP_ERR="/tmp/push_swap_test_stderr"
TMP_VALGRIND="/tmp/push_swap_test_valgrind"
COLOR_RESET="\033[0m"
COLOR_PASS="\033[38;5;46m"
COLOR_FAIL="\033[38;5;160m"
TOTAL_TESTS=0
FAILED_TESTS=0
VALGRIND_EXIT_CODE=99

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

run_case()
{
	label="$1"
	expected_code="$2"
	shift 2

	./test "$@" >"$TMP_OUT" 2>"$TMP_ERR"
	actual_code=$?
	valgrind --leak-check=full --show-leak-kinds=all \
		--errors-for-leak-kinds=all --error-exitcode="$VALGRIND_EXIT_CODE" \
		--log-file="$TMP_VALGRIND" ./test "$@" >/dev/null 2>/dev/null
	valgrind_code=$?
	TOTAL_TESTS=$((TOTAL_TESTS + 1))
	case_failed=0

	echo "----------------------------------------"
	echo "Test: $label"
	if [ "$actual_code" -eq "$expected_code" ]
	then
		print_status "Program status" 1
	else
		print_status "Program status" 0
		case_failed=1
	fi
	if [ "$valgrind_code" -eq "$expected_code" ]
	then
		print_status "Valgrind status" 1
	else
		print_status "Valgrind status" 0
		case_failed=1
	fi
	if [ "$case_failed" -eq 1 ]
	then
		FAILED_TESTS=$((FAILED_TESTS + 1))
	fi

	echo "Command: ./test $*"
	echo "Expected return code: $expected_code"
	echo "Actual return code: $actual_code"
	echo "Valgrind return code: $valgrind_code"

	if [ -s "$TMP_OUT" ]
	then
		echo "Standard output:"
		cat "$TMP_OUT"
		printf "\n"
	else
		echo "Standard output: <empty>"
	fi

	if [ -s "$TMP_ERR" ]
	then
		echo "Standard error:"
		cat "$TMP_ERR"
		printf "\n"
	else
		echo "Standard error: <empty>"
	fi

	if [ -s "$TMP_VALGRIND" ]
	then
		echo "Valgrind log:"
		cat "$TMP_VALGRIND"
		printf "\n"
	else
		echo "Valgrind log: <empty>"
	fi
}

echo -e "\n[1/3] Building archive\n"
if ! make re
then
	echo "Build failed"
	exit 1
fi

echo -e "\n[2/3] Linking test binary\n"
if ! cc -Wall -Wextra -Werror push_swap.a -o test
then
	echo "Link failed"
	exit 1
fi

echo -e "\n[3/3] Running functional and valgrind tests\n"
run_case "No arguments" 0
run_case "Empty string" 0 ""
run_case "Spaces only" 0 "   "
run_case "Valid quoted input" 0 "3 -5 1 7 -2 -8 4 -1 6 -6 0 5 -3 2 -7 -4"
run_case "Valid split arguments" 0 3 -5 1 7 -2 -8 4 -1 6 -6 0 5 -3 2 -7 -4
run_case "Duplicate value" 1 1 2 3 2
run_case "Invalid token" 1 1 2 a 4
run_case "Sign only" 1 +
run_case "Maximum integer" 0 2147483647
run_case "Minimum integer" 0 -2147483648
run_case "Overflow above maximum integer" 1 2147483648
run_case "Underflow below minimum integer" 1 -2147483649
run_case "Huge positive number" 1 999999999999999999999999999999999999999999999999
run_case "Huge negative number" 1 -999999999999999999999999999999999999999999999999

echo "----------------------------------------"
echo "Total tests: $TOTAL_TESTS"
echo "Failed tests: $FAILED_TESTS"
echo "Passed tests: $((TOTAL_TESTS - FAILED_TESTS))"

if [ "$FAILED_TESTS" -eq 0 ]
then
	echo -e "Overall result: ${COLOR_PASS}Passed${COLOR_RESET}"
	exit 0
fi

echo -e "Overall result: ${COLOR_FAIL}Failed${COLOR_RESET}"
exit 1
