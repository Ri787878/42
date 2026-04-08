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

//ex05
char int_to_char(int n)
{
	char c;

	c = n +'0';
	return c;
}

//ex06
void    write_number(int cen, int dez, int uni)
{
        ft_putchar(cen + '0');
        ft_putchar(dez + '0');
        ft_putchar(uni + '0');
        ft_putchar(',');
        ft_putchar(' ');
}

void    ft_print_comb(void)
{
        int     centenas;
        int     dezenas ;
        int     unidades;

        centenas = 0;
        dezenas = 1;
        unidades = 2;
        while (centenas < dezenas && centenas <= 9)
        {
                while (dezenas < unidades && dezenas <= 9)
                {
                        while (unidades <= 9)
                        {
                                write_number(centenas, dezenas, unidades);
                                unidades += 1;
                        }
                        dezenas += 1;
                        unidades = dezenas + 1;
                }
                centenas += 1;
                dezenas = centenas + 1;
                unidades = dezenas + 1;
        }
}

int main ()
{
	ft_print_comb();
	return 0;
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






int main ()
{
	int num = 12;
	int centenas;
	int dezenas ;
	int unidades;

	centenas = cal_cen(num);
	dezenas = cal_dez(num);
	unidades = cal_uni(num);
	char c = 0;
	while (centenas < 10)
	{
	    while (dezenas != 0)
	    {
	        while ( unidades != 0)
	        {
				c = int_to_char(centenas);
				write(1, &c, 1);
				c = int_to_char(dezenas);
				write(1, &c, 1);
				c = int_to_char(unidades);
				write(1, &c, 1);
				write(1, ", ", 2);
	            num += 1;
				unidades = cal_uni(num);

	        }
			num = num + dezenas + 1;
			unidades = cal_uni(num);
			dezenas = cal_dez(num);
	    }
		num = num + centenas + 1;
		unidades = cal_uni(num);
		dezenas = cal_dez(num);
		centenas = cal_cen(num);
	}
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
