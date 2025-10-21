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

//ex02
void	ft_print_reverse_alphabet(void)
{
	write(1, "zyxwvutsrqponmlkjihgfedcba", 26);
}

//ex03
void    ft_print_numbers(void)
{
        write(1, "0123456789", 10);
}

//ex04
void    ft_is_negative(int n)   
{
        if (n < 0)
                write(1, "N", 1);
        else if (n >= 0)
                write(1, "P", 1);
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

//main ex01

int main ()
{
        ft_print_alphabet();
        return 0;
}


//main for ex02
int main()
{
	ft_print_reverse_alphabet();
	return 0;
}


//main for ex03
int main()
{
	ft_print_numbers();
	return 0;
}
*/

//main for ex04
int main()
{
	int pos = 10;
	int neg = -10;
	int zero = 0;
	ft_is_negative(pos);
	write(1, "\n", 1);
	ft_is_negative(neg);
	write(1, "\n", 1);
	ft_is_negative(zero);

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
