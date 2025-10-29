/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_itoa.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/29 11:20:04 by ridias            #+#    #+#             */
/*   Updated: 2025/10/29 12:39:53 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	int_size(int nb)
{
	int	n;

	n = 1;
	while (nb / 10 != 0)
	{
		nb = nb / 10;
		n++;
	}
	return (n);
}

int	ft_pow(int base, int exp)
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

long	handle_sign(int n, int *sign)
{
	long	num;

	num = n;
	if (n < 0)
	{
		*sign = -1;
		num = -num;
	}
	return (num);
}

char	*ft_itoa(int n)
{
	int		sign;
	long	num;
	int		nbr_size;
	char	*nbr;
	int		t;

	t = 0;
	sign = 0;
	num = handle_sign(n, &sign);
	nbr_size = int_size(n);
	nbr = malloc((nbr_size - sign + 1) * sizeof(char));
	if (sign == -1)
		nbr[t++] = '-';
	while (nbr_size != 0)
	{
		nbr[t] = (num / ft_pow(10, nbr_size - 1) + '0');
		num = num - (nbr[t] - '0') * ft_pow(10, nbr_size - 1);
		nbr_size--;
		t++;
	}
	nbr[t] = '\0';
	return (nbr);
}
