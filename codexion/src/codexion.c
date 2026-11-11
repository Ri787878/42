# include "codexion.h"


void	runtime(struct codexionStruct *cdx){
	(void)cdx;
	while (true){
		break;
	}
}


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
	//runtime(cdx);
	pthread_join(cdx->monitor_thread, NULL);
	free_codexion_struct(cdx);
	return (1);
}
