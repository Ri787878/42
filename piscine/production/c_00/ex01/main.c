#include <stdio.h>
#include <unistd.h>

//ex00
void	ft_putchar(char c)
{
	write(1, &c, 1);
}

//ex01
void    ft_print_alphabet(void)
{
        write(1, "abcdefghijklmnopqrstuvwxyz", 26);
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
//main ex01
/*
int main ()
{
        ft_print_alphabet();
        return 0;
}
*/

//main for ex02
int main()
{
	return 0;
}


/*
 	printf("You have entered %d arguments:\n", argc - 1);
        while   ( i < argc)
        {
                printf("%s\n", argv[i]);
                i++;
        }
 * */
