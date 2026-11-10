# include "../src/codexion.h"
#include <assert.h>


int	codexion(long int argc, char** argv)
{
	struct codexionStruct *cdx;
	int	parse_code;

	if (argv == NULL){
		printf("[PARCING ERROR CODE -2] No arguments passed!\n");
		return (-2);
	}
	if (argc != 9){
		printf("[PARCING ERROR CODE -9] Argument amount isn't right!\n");
		return (-9);
	}
	cdx = init_codexion_struct(argc, argv);
	if (cdx == NULL)
		return (-2);
	parse_code = parse_arguments(cdx);
	free_codexion_struct(cdx);
	if (parse_code <= 0)
		return (parse_code);
	return (-1);
}

void	test_codexion_argument_types()
{
	char *empty_pointer[9] = { "codexion", "", "10", "100", "200", "50", "30", "10", "fifo" };
	char *empty_string[9] = { "codexion", " ", "10", "100", "200", "50", "30", "10", "fifo" };

	assert(codexion(9, empty_pointer) == -2);
    assert(codexion(9, empty_string) == -2);
    assert(codexion(9, NULL) == -2);

	// Array of invalid type representations to test against
    char *invalid_types[] = {
        "abc",   // str
        "true",  // bool
        "x",     // char
        " ",     // space
        "",      // empty string
        "3.14",  // float
        NULL     // void
    };
    int num_invalid_types = 7;

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
            if (pos == 8 && t != 6)
                assert(codexion(9, test_argv) == -3);
            else
                assert(codexion(9, test_argv) == -2);
        }
    }

    printf("\nAll matrix position and invalid type tests passed successfully!\n\n");
}

void test_codexion_argument_quantities(void) {
    char *emt = "";

	assert(codexion(0, &emt) == -9);
    assert(codexion(10, &emt) == -9);
    assert(codexion(1000, &emt) == -9);

    printf("\nAll argument quantity assertions passed successfully!\n\n");
}

void	test_parcer()
{
	test_codexion_argument_quantities();
	test_codexion_argument_types();
}


int main()
{
	test_parcer();
}
