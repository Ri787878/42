# include "../src/codexion.h"


int	codexion(int argc, char** arguments)
{
	int	parse_code;

	parse_code = parse_arguments(argc, arguments);
	if (parse_code <= 0)
		return (parse_code);
	return (-1);
}


void	test_invalid_quantity_of_inputs()
{
	char *emt = "";
	// char *empty_pointer = "\0";
	// char *empty_string = " ";

	printf("0 args: %d expected -9\n", codexion(0, &emt));
	printf("-10 args: %d expected -9\n", codexion(-10, &emt));
	printf("10 args: %d expected -9\n", codexion(10, &emt));
	printf("2147483649 args: %d expected -9\n", codexion(2147483649, &emt));
	printf("-2147483648 args: %d expected -9\n", codexion(-2147483648, &emt));

	// to test for invalid types
	//	printf("Empty pointer: %d expected -2\n", codexion(0, &empty_pointer));
	//	printf("Empty string: %d expected -2\n", codexion(0, &empty_string));
}


void	test_parcer()
{
	// Test invalid number of arguments
	test_invalid_quantity_of_inputs();
}


int main()
{
	test_parcer();
}
