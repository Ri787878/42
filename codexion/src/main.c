# include "codexion.h"


int main(int argc, char** argv)
{
	char *emt = "";

	printf("res=%d\n", codexion(0, &emt));
	return (codexion(argc, argv));
}
