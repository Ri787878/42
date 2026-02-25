/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putnbr_fd.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 16:25:41 by ridias            #+#    #+#             */
/*   Updated: 2025/10/30 16:41:23 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

static int	int_size(int nb)
{
	int	n;

	n = 0;
	while (nb / 10 != 0)
	{
		nb = nb / 10;
		n++;
	}
	return (n);
}

static int	ft_pow(int base, int exp)
{
	int	result;

	result = 1;
	while (exp > 0)
	{
		result *= base;
		exp--;
	}
	return (result);
}

static int	check_nb(int nb, int fd)
{
	if (nb == -2147483648)
	{
		ft_putstr_fd("-2147483648", fd);
		return (-2147483648);
	}
	if (nb == 0)
	{
		ft_putchar_fd('0', fd);
		return (-2147483648);
	}
	return (nb);
}

void	ft_putnbr_fd(int n, int fd)
{
	int	nb_size;
	int	res;

	nb_size = int_size(n);
	if (check_nb(n, fd) == -2147483648)
		return ;
	if (n < 0)
	{
		ft_putchar_fd('-', fd);
		n = -n;
	}
	while (nb_size != 0)
	{
		res = n / ft_pow(10, nb_size);
		ft_putchar_fd(res + '0', fd);
		n = n - res * ft_pow(10, nb_size);
		nb_size--;
	}
	ft_putchar_fd((n % 10) + '0', fd);
}
