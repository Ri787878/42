/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sqrt.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/09/23 14:17:09 by ridias            #+#    #+#             */
/*   Updated: 2025/09/24 15:44:01 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_sqrt(int nb)
{
	int	counter;

	counter = 0;
	if (nb == 1)
		return (1);
	while (counter < nb)
	{
		if (counter * counter == nb)
			return (counter);
		counter++;
	}
	return (0);
}

/*
int main(void)
{
	int	i = -1;
	while (i <= 1000)
	{
		if (ft_sqrt(i) != 0 || i <= 0)
			printf("%d = %d\n", i, ft_sqrt(i));
		i++;
	}
	return (0);
}
*/