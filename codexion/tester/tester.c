# include "../src/codexion.h"
#include <assert.h>
#include <unistd.h>

static int	run_and_capture(char **arguments, char *output, size_t output_size)
{
	FILE	*capture;
	int		saved_stdout;
	int		result;
	size_t	bytes_read;

	capture = tmpfile();
	assert(capture != NULL);
	fflush(stdout);
	saved_stdout = dup(STDOUT_FILENO);
	assert(saved_stdout >= 0);
	assert(dup2(fileno(capture), STDOUT_FILENO) >= 0);
	result = codexion(9, arguments);
	fflush(stdout);
	assert(dup2(saved_stdout, STDOUT_FILENO) >= 0);
	close(saved_stdout);
	rewind(capture);
	bytes_read = fread(output, 1, output_size - 1, capture);
	output[bytes_read] = '\0';
	assert(!ferror(capture));
	fclose(capture);
	return (result);
}

static int	count_events(const char *output, const char *event)
{
	int			count;
	const char	*match;

	count = 0;
	match = output;
	while ((match = strstr(match, event)) != NULL)
	{
		count++;
		match += strlen(event);
	}
	return (count);
}

static void	test_single_coder_burnout(void)
{
	char	*arguments[9] = {
		"codexion", "1", "10", "7", "4", "4", "1", "1", "fifo"
	};
	char	output[1024];

	assert(run_and_capture(arguments, output, sizeof(output)) == 1);
	assert(count_events(output, " 1 burned out\n") == 1);
	assert(count_events(output, " is compiling\n") == 0);
	printf("\n[SINGLE CODER BURNOUT] Expected: coder 1 burns out without compiling. Passed.");
}

static void	test_fifo_completion(void)
{
	char	*arguments[9] = {
		"codexion", "2", "500", "1", "1", "1", "1", "1", "fifo"
	};
	char	output[1024];

	assert(run_and_capture(arguments, output, sizeof(output)) == 1);
	assert(count_events(output, " is compiling\n") == 2);
	assert(count_events(output, " 1 is compiling\n") == 1);
	assert(count_events(output, " 2 is compiling\n") == 1);
	assert(count_events(output, " has taken a dongle\n") == 4);
	assert(count_events(output, " burned out\n") == 0);
	printf("\n[FIFO COMPLETION] Expected: both coders compile once; no burnout. Passed.");
}

static void	test_edf_work_cycles(void)
{
	char	*arguments[9] = {
		"codexion", "2", "1000", "1", "1", "1", "2", "1", "edf"
	};
	char	output[1024];

	assert(run_and_capture(arguments, output, sizeof(output)) == 1);
	assert(count_events(output, " is compiling\n") == 4);
	assert(count_events(output, " 1 is compiling\n") == 2);
	assert(count_events(output, " 2 is compiling\n") == 2);
	assert(count_events(output, " is debugging\n") == 2);
	assert(count_events(output, " 1 is debugging\n") == 1);
	assert(count_events(output, " 2 is debugging\n") == 1);
	assert(count_events(output, " is refactoring\n") == 2);
	assert(count_events(output, " 1 is refactoring\n") == 1);
	assert(count_events(output, " 2 is refactoring\n") == 1);
	assert(count_events(output, " burned out\n") == 0);
	printf("\n[EDF WORK CYCLES] Expected: both coders compile twice, with one debug and refactor each. Passed.");
}

static void	test_ten_coder_completion(void)
{
	char	*arguments[9] = {
		"codexion", "10", "5000", "1", "1", "1", "1", "1", "fifo"
	};
	char	output[4096];
	char	expected_event[64];
	int		coder;

	assert(run_and_capture(arguments, output, sizeof(output)) == 1);
	assert(count_events(output, " is compiling\n") == 10);
	assert(count_events(output, " has taken a dongle\n") == 20);
	assert(count_events(output, " burned out\n") == 0);
	coder = 1;
	while (coder <= 10)
	{
		snprintf(expected_event, sizeof(expected_event),
			" %d is compiling\n", coder);
		assert(count_events(output, expected_event) == 1);
		coder++;
	}
	printf("\n[TEN CODER COMPLETION] Expected: all 10 coders compile once without burnout. Passed.");
}

void	test_codexion_argument_types()
{
	char *empty_pointer[9] = { "codexion", "", "10", "100", "200", "50", "30", "10", "fifo" };
	char *empty_string[9] = { "codexion", " ", "10", "100", "200", "50", "30", "10", "fifo" };

	assert(codexion(9, empty_pointer) < 0);
    assert(codexion(9, empty_string) < 0);

	// Array of invalid type representations to test against
    char *invalid_types[] = {
        "abc",   // str
        "true",  // bool
        "x",     // char
        " ",     // space
        "",      // empty string
        "3.14"   // float
    };
    int num_invalid_types = 6;

    // Default valid arguments template (index 0 is program name "codexion")
    // Positions 1 through 8: number_of_coders, number_of_compiles, time_to_burnout,
    // time_to_compile, time_to_debug, time_to_refactor, dongle_cooldown, scheduler/etc.
    char *base_args[9] = { "codexion", "5", "10", "100", "200", "50", "30", "10", "fifo" };

    // Loop through every position from 1 to 8
    for (int pos = 1; pos <= 8; pos++) {
        // Loop through every invalid type
        for (int t = 0; t < num_invalid_types; t++) {

            // 1. Create a fresh local char *argv[] array for this test case
            char *test_argv[9];
            for (int i = 0; i < 9; i++) {
                test_argv[i] = base_args[i]; // Copy defaults
            }

            // 2. Inject the invalid type into the current position
            test_argv[pos] = invalid_types[t];

            // 3. Assert that codexion correctly identifies it and returns -2
            if (pos == 8)
                assert(codexion(9, test_argv) < 0);
            else
                assert(codexion(9, test_argv) < 0);
        }
    }
}

void test_codexion_argument_quantities(void) {
    char *too_many_args[1001];
    int i;

    too_many_args[0] = "codexion";
    i = 1;
    while (i < 1000)
        too_many_args[i++] = "extra";
    too_many_args[10] = NULL;
    assert(codexion(10, too_many_args) < 0);
    too_many_args[10] = "extra";
    too_many_args[1000] = NULL;
    assert(codexion(1000, too_many_args) < 0);
}

void test_codexion_argument_ranges(void){
	char *base_args[9] = {
		"codexion", "5", "10", "100", "200", "50", "30", "10", "fifo"
	};
	char *test_args[9];
	int	pos;

	for (pos = 0; pos < 9; pos++)
		test_args[pos] = base_args[pos];
	test_args[1] = "0";
	assert(codexion(9, test_args) < 0);

	for (pos = 1; pos <= 7; pos++) {
		test_args[pos] = "-1";
		assert(codexion(9, test_args) < 0);
		test_args[pos] = base_args[pos];
	}

	for (pos = 1; pos <= 7; pos++)
		test_args[pos] = "0";
	test_args[1] = "1";
	assert(codexion(9, test_args) > 0);

	test_args[8] = "round_robin";
	assert(codexion(9, test_args) < 0);
	test_args[8] = "FIFO";
	assert(codexion(9, test_args) < 0);
	test_args[8] = "";
	assert(codexion(9, test_args) < 0);
	test_args[8] = "edf";
	assert(codexion(9, test_args) > 0);
}

void	test_parcer()
{
	test_codexion_argument_quantities();
	test_codexion_argument_types();
	test_codexion_argument_ranges();
	test_single_coder_burnout();
	test_fifo_completion();
	test_edf_work_cycles();
	test_ten_coder_completion();
	
    printf("\n[ARGUMENT QUANTITY TEST] All argument quantity assertions passed successfully!");
    printf("\n[ARGUMENT TYPES TEST] All matrix position and invalid type tests passed successfully!");
	printf("\n[ARGUMENT RANGE TEST] All argument range assertions passed successfully!");
	printf("\n\n[FINAL RESULT] All parcer tests passed!!\n");
}


int main()
{
	test_parcer();
}
