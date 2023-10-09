/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_rev_int_tab.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/07/30 12:14:07 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/07/31 10:13:03 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_rev_int_tab(int *tab, int size)
{
	int	beg;
	int	end;
	int	caar;

	beg = 0;
	end = size;
	while (beg < end)
	{
		caar = tab[beg];
		tab[beg] = tab[end - 1];
		tab[end - 1] = caar;
		end--;
		beg++;
	}
}
/*
int main()
{
	//Main de teste do exercicio ex07
	int tab[10] = {-44, 65, 0, -1, 100, -44, 65, 0, -1, 100};
	int size = sizeof(tab) / 4;
	int i = 0;

	printf("A sequencia: ");
	
	while(i < size){
		printf("%d ", tab[i]);
		i++;
	}
	printf("de %d digitos.", size);
	i = 0;

	printf("\n");

	ft_rev_int_tab(tab, size);

	printf("Quando apanha com um uno reverse fica: ");
	
	while(i < size){
		printf("%d ", tab[i]);
		i++;
	}
	printf("\n");
}
*/
