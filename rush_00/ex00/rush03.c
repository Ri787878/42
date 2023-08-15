/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush03.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/07/30 15:59:37 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/07/30 16:21:53 by joandre-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_putchar(char c);

void	cantos(int coluna, int linha, int x, int y)
{
	if (linha == 0 && coluna == 0)
		ft_putchar('A');
	if (x > 1 && linha == 0 && coluna == x - 1)
		ft_putchar('C');
	if (y > 1)
	{
		if (linha == y - 1 && coluna == 0)
			ft_putchar('A');
		if (coluna > 1 && linha == y - 1 && coluna == x - 1)
			ft_putchar('C');
	}
	if (coluna > 0 && coluna < x - 1 && (linha == 0 || linha == y - 1))
		ft_putchar('B');
}

void	colunas(int coluna, int linha, int x, int y)
{
	if ((linha > 0 && linha < y - 1) && (coluna == 0 || coluna == x - 1))
		ft_putchar('B');
	if (coluna > 0 && coluna < x - 1 && (linha > 0 && linha < y - 1))
		ft_putchar(' ');
}

void	rush(int x, int y)
{
	int	coluna;
	int	linha;

	coluna = 0;
	linha = 0;
	if (x <= 0 && y <= 0)
		return ;
	if (x == 1 && y == 1)
		ft_putchar('A');
	else
	{
		while (linha < y)
		{
			while (coluna < x)
			{
				cantos(coluna, linha, x, y);
				colunas(coluna, linha, x, y);
				coluna++;
			}
			ft_putchar('\n');
			linha++;
			coluna = 0;
		}
	}
}
