# include "codexion.h"


int	codexion(long int argc, char** argv)
{
	struct codexionStruct *cdx;
	int	parse_code;

	cdx = init_codexion_struct(argc, argv);
	if (cdx == NULL)
		return (-2);
	parse_code = parse_arguments(cdx);
	if (parse_code <= 0)
		return (parse_code);
	printf("parse code = %d", parse_code);
	print_struct(cdx);
	free_codexion_struct(cdx);
	return (1);
}


int main(int argc, char** argv)
{
	return (codexion(argc, argv));
}
