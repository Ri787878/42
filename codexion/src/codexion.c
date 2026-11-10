# include "codexion.h"


int	codexion(long int argc, char** argv)
{
	struct codexionStruct *cdx;
	int	parse_code;

	cdx = init_codexion_struct(argc, argv);
	if (cdx == NULL)
		return (-30);
	parse_code = parse_arguments(cdx);
	if (parse_code <= 0) {
		free_codexion_struct(cdx);
		return (parse_code);
	}
	if (validate_numbers(cdx) < 0) {
		free_codexion_struct(cdx);
		return (-24);
	}
	print_struct(cdx);
	free_codexion_struct(cdx);
	return (1);
}


int main(int argc, char** argv)
{
	char *emt = "";

	printf("res=%d\n", codexion(0, &emt));
	return (codexion(argc, argv));
}
