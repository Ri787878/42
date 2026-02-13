/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf_helper2.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/13 23:38:06 by ridias            #+#    #+#             */
/*   Updated: 2025/11/14 00:18:06 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	ft_put_unsigned(unsigned int nb)
{
	int		counter;
	char	c;

	counter = 0;
	if (nb >= 10)
		counter += ft_put_unsigned(nb / 10);
	c = nb % 10 + '0';
	counter += write(1, &c, 1);
	return (counter);
}

int	ft_convert_uint_to_hexa_small(unsigned int nb)
{
	int		c;
	int		counter;
	char	*hexa_index;

	counter = 0;
	hexa_index = "0123456789abcdef";
	if (nb >= 16)
		counter += ft_convert_uint_to_hexa_small(nb / 16);
	c = hexa_index[nb % 16];
	counter += write(1, &c, 1);
	return (counter);
}

int	ft_convert_uint_to_hexa_big(unsigned int nb)
{
	int		c;
	int		counter;
	char	*hexa_index;

	counter = 0;
	hexa_index = "0123456789ABCDEF";
	if (nb >= 16)
		counter += ft_convert_uint_to_hexa_big(nb / 16);
	c = hexa_index[nb % 16];
	counter += write(1, &c, 1);
	return (counter);
}

int	check_char(const char *format, int t, va_list args)
{
	if (format[t] == 'c')
		return (ft_putchar(va_arg(args, int)));
	if (format[t] == 's')
		return (ft_putstr(va_arg(args, char *)));
	if (format[t] == 'p')
		return (ft_putpointer(va_arg(args, size_t)));
	if (format[t] == 'd' || format[t] == 'i')
		return (ft_putnbr(va_arg(args, int)));
	if (format[t] == 'u')
		return (ft_put_unsigned(va_arg(args, unsigned int)));
	if (format[t] == 'x')
		return (ft_convert_uint_to_hexa_small(va_arg(args, unsigned int)));
	if (format[t] == 'X')
		return (ft_convert_uint_to_hexa_big(va_arg(args, unsigned int)));
	if (format[t] == '%')
		return (ft_putchar(format[t]));
	else
		return (0);
}
