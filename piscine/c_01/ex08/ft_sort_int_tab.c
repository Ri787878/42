/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sort_int_tab.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/07/31 09:09:53 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/07/31 10:18:40 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_sort_int_tab(int *tab, int size)
{
	int	i;
	int	j;
	int	temp;

	i = 0;
	j = 1;
	while (i < size)
	{
		while (j < size)
		{
			if (tab[j - 1] > tab[j])
			{
				temp = tab[j];
				tab[j] = tab[j - 1];
				tab[j - 1] = temp;
			}
			j++;
		}
		j = 1;
		i++;
	}
}

/*
int main(void)
{
	int tab[10] = {-100, -4, 54, 664, 33, 22, 21, -1000, 2, 5};
	int n1;
	int i;

	n1 = sizeof(tab) / 4;
	i = 0;
	printf("A sequencia: ");
	while(i < n1)
	{
		printf("%d ", tab[i]);
		i++;
	}
	printf("de %d digitos.\n", n1);
	i = 0;
	ft_sort_int_tab(tab, n1);
	printf("\n");
	printf("Quando organizada em ordem crescente fica em: ");
	while(i < n1)
	{
		printf("%d ", tab[i]);
		i++;
	}
	printf("\n");
}
*/
