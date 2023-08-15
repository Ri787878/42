/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_div_mod.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/07/30 12:02:58 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/07/30 12:04:06 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_ultimate_div_mod(int *a, int *b)
{
	int	temp1;
	int	temp2;

	temp1 = *a / *b;
	temp2 = *a % *b;
	*a = temp1;
	*b = temp2;
}
/*
int main(void)
{
//Main de teste do exercicio ex04

    int n1 = 23;
    int n2 = 10;
    int *p1;
    int *p2;

    p1 = &n1;
    p2 = &n2;


    printf("O 1º numero atual = %d, e o 2º numero atual = %d \n", *p1, *p2);

    ft_ultimate_div_mod(p1, p2);

    printf("Que divididos resultam em = %d, sendo o resto = %d \n",*p1, *p2);
}
*/
