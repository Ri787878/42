#include <stdio.h>
#include <unistd.h>

void	ft_putchar(char c)
{
	write(1, &c, 1);
}
//main for ex00
/*
int main (int argc, char *argv[])
{
	char c1;
	c1 = argv[1][0];

	ft_putchar(c1);
	return 0;
}

*/


/*
 	printf("You have entered %d arguments:\n", argc - 1);
        while   ( i < argc)
        {
                printf("%s\n", argv[i]);
                i++;
        }
 * */
