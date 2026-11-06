# include "../src/codexion.h"


void	test_invalid_quantity_of_inputs()
{
	codexion("\0");
	codexion(" ");
	codexion(NULL);
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
