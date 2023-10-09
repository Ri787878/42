/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   rush00.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/07/30 16:05:01 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/07/30 17:29:44 by joandre-         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

void	ft_putchar(char c);

void	cantos(int coluna, int linha, int x, int y)
{
	if (linha == 0 && coluna == 0)
		ft_putchar('o');
	if (x > 1 && linha == 0 && coluna == x - 1)
		ft_putchar('o');
	if (y > 1)
	{
		if (linha == y - 1 && coluna == 0)
			ft_putchar('o');
		if (coluna > 1 && linha == y - 1 && coluna == x - 1)
			ft_putchar('o');
	}
	if (coluna > 0 && coluna < x - 1 && (linha == 0 || linha == y - 1))
		ft_putchar('-');
}

void	colunas(int coluna, int linha, int x, int y)
{
	if ((linha > 0 && linha < y - 1) && (coluna == 0 || coluna == x - 1))
		ft_putchar('|');
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
		ft_putchar('o');
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
