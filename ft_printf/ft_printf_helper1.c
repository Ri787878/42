/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_helper1.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 15:29:08 by ridias            #+#    #+#             */
/*   Updated: 2025/11/14 00:07:30 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_putchar(const char c)
{
	write(1, &c, 1);
	return (1);
}

int	ft_putstr(char *s)
{
	int	n;

	if (!s)
		return (ft_putstr("(null)"));
	n = 0;
	while (s[n] != '\0')
	{
		ft_putchar(s[n]);
		n++;
	}
	return (n);
}

int	ft_putnbr(int nb)
{
	int		counter;
	char	c;

	counter = 0;
	if (nb == -2147483648)
	{
		counter += write(1, "-2147483648", 11);
		return (counter);
	}
	if (nb < 0)
	{
		counter += write(1, "-", 1);
		nb = -nb;
	}
	if (nb >= 10)
		counter += ft_putnbr(nb / 10);
	c = (nb % 10) + '0';
	counter += write(1, &c, 1);
	return (counter);
}

int	ft_putpointer(size_t pointer)
{
	int		counter;

	if (pointer == 0)
		return (ft_putstr("0x0"));
	counter = 0;
	counter += ft_putstr("0x");
	counter += ft_put_hexa_nbr(pointer);
	return (counter);
}

int	ft_put_hexa_nbr(size_t pointer)
{
	int		c;
	int		counter;
	char	*hexa_index;

	counter = 0;
	hexa_index = "0123456789abcdef";
	if (pointer >= 16)
		counter += ft_put_hexa_nbr(pointer / 16);
	c = hexa_index[pointer % 16];
	counter += write(1, &c, 1);
	return (counter);
}
