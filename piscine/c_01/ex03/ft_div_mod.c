/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_div_mod.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/07/30 12:02:23 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/07/30 12:02:32 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_div_mod(int a, int b, int *div, int *mod)
{
	*div = a / b;
	*mod = a % b;
}
/*
int main(void)
{
//Main de teste do exercicio ex03

    int n1 = 23;
    int n2 = 10;
    int n3 = 0;
    int n4 = 0;
    int *p1;
    int *p2;

    p1 = &n3;
    p2 = &n4;


    printf("O 1º numero atual = %d, e o 2º numero atual = %d \n", n1, n2);

    ft_div_mod(n1, n2, p1, p2);

    printf("Que divididos resultam em = %d, sendo o resto = %d \n", n3, n4);
}
*/
