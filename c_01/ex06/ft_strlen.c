/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlen.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/07/30 12:10:14 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/07/30 12:13:36 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i] != '\0')
	{
		i++;
	}
	return (i);
}

void	ft_putstr(char *str)
{
	int	i;

	i = 0;
	while (i <= ft_strlen(str))
	{
		write(1, &str[i], 1);
		write(1, " ", 1);
		i++;
	}
}
/*
int main(void){
    
//Main de teste do exercicio ex06
char *s1 = "abcdefghijklmnopqrstuvwxyz";
char **p1;
int n1;
p1 = &s1;
printf("A palavra %s, ",*p1);
n1 = ft_strlen(s1);
printf("tem %d letras. \n", n1);   
}
*/
