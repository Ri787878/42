/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_swap.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/07/30 12:01:13 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/07/30 12:01:24 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_swap(int *a, int *b)
{
	int	temp;

	temp = *a;
	*a = *b;
	*b = temp;
}
/*
//Main de teste do exercicio ex02
int main(void)
{
    int n1 = 10;
    int n2 = 20;
    int *p1 = &n1;
    int *p2 = &n2;


    printf("O 1º numero atual = %d, e o 2º numero atual = %d \n", n1, n2);

    ft_swap(p1, p2);

    printf("E depois = %d, e = %d \n", n1, n2);
}
*/
