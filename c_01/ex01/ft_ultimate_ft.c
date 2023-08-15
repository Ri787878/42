/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_ultimate_ft.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/07/30 11:57:25 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/07/31 10:28:15 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_ultimate_ft(int *********nbr)
{
	int	n1;
	int	*p1;

	n1 = 42;
	p1 = &n1;
	*********nbr = *p1;
}
/*
int main(void)
{
// Main de teste do exercicio ex01

    int n1;
    int *p1;
    int **p2;
    int ***p3;
    int ****p4;
    int *****p5;
    int ******p6;
    int *******p7;
    int ********p8;
    int *********p9;
    
    p9 = &p8;
    p8 = &p7;
    p7 = &p6;
    p6 = &p5;
    p5 = &p4;
    p4 = &p3;
    p3 = &p2;
    p2 = &p1;
    p1 = &n1;
    n1 = 10;

    printf("O numero atual = %d \n", n1);

    ft_ultimate_ft(p9);

    printf("E depois = %d \n", n1);
}
*/
