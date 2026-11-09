# include "../codexion.h"


int parse_arguments(int argc, char *argv[])
{
	int c;

	c = 0;
	if (argc != 9)
		return (-9);
	while (c < 9){
		if (!ft_isdigit(ft_atoi(argv[c])))
			return (-2);
		c++;
	}
	return (-1);
}
