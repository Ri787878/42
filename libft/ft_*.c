/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: rmano-cl <rmano-cl@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/10/03 14:50:57 by rmano-cl          #+#    #+#             */
/*   Updated: 2023/10/16 13:47:01 by rmano-cl         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"


/*
Allocates (with malloc(3)) and returns a substring
from the string ’s’.
The substring begins at index ’start’ and is of
maximum size ’len’.
*/
char *ft_substr(char const *s, unsigned int start, size_t len)
{
	char	*substr;
	size_t	i;

	if (!s)
		return (ft_strdup(""));
	if (start > ft_strlen(s))
		return (ft_strdup(""));
	substr = (char *)malloc(sizeof(char) * (len + 1));
	if (!substr)
		return (NULL);
	i = 0;
	while (i < len && s[start + i])
	{
		substr[i] = s[start + i];
		i++;
	}
	substr[i] = 0;
	return (substr);
}



int	main(void){


	return (0);
}
/*
ft_isalpha
    char c1 = 'a';
    printf("%d\n", ft_isalpha(c1));
    printf("%d\n", isalpha(c1));

ft_isdigit
    char c2 = '1';

    printf("%d\n", ft_isdigit(c2));
    printf("%d\n", isdigit(c2));

ft_isalnum
    char c3 = 'z';
    printf("%d\n", ft_isalnum(c3));
    printf("%d\n", isalnum(c3));

ft_isascii
    char c4 = 'a';
    printf("%d\n", ft_isascii(c4));
    printf("%d\n", isascii(c4));

ft_isprint
    char c5 = 'a';

    printf("%d\n", ft_isprint(c5));
    printf("%d\n", isprint(c5));

ft_strlen
    char *s1 = "abcdefghijklmnopqrstuvwxyz";
    char **p1;
    int n1;

    p1 = &s1;
    printf("A palavra %s, ",*p1);
    n1 = ft_strlen(s1);
    printf("tem %d letras. \n", n1);

ft_memset
    char s2[] = "abcdefghijklmnopqrstuvwxyz";

    printf("%s\n", s2);
    ft_memset(s2, '&', 25);
    printf("%s\n", s2);

ft_bzero
    char s2[] = "abcdefghijklmnopqrstuvwxyz";

    printf("%s\n", s2);
    ft_bzero(s2, 2);
    printf("%s\n", s2);

ft_memcpy

    char s2[] = "abcdefghijklmnopqrstuvwxyz";
    char s3[] = "123456789";

    printf("\n");
    printf("%s\n", s2);
    ft_memcpy(s2 + 5, s3, 5);
    printf("%s\n", s2);

//ft_memmove

 printf("-------------------------//----------------------------\n");
    char s4[] = "abcdefghijklmnopqrstuvwxyz";
    char s5[] = "123456789";
    char s6[] = "abcdefghijklmnopqrstuvwxyz";
    char s7[] = "123456789";

    printf("Correct version:\n");
    printf("%s\n", s4);
    ft_memmove(s4 + 6, s5, 5);
    printf("%s\n", s4);
    printf("\nMy version version:\n");
    printf("%s\n", s6);
    memmove(s6 + 6, s7, 5);
    printf("%s\n", s6);

//ft_strlcpy
    size_t mine = 0;
    char s1[10] = "abc";
    char s2[10] = "defgh";
    //char *correct = 0;

    mine = ft_strlcpy(s1, s2, 2);
    //correct = strncpy("abc", "defgh", 3);

printf("My func returns: %ld.\n", mine);

//ft_strlcat
    size_t  mine = 0;
    char s1[10] = "abc";
    char s2[10] = "defgh";

    mine = ft_strlcat(s1, s2, 2);
    printf("My func returns: %ld.\n", mine);

ft_toupper
    char c1 = 'a';
    printf("%c\n", ft_toupper(c1));
    printf("%c\n", toupper(c1));

ft_tolower
    char c1 = 'A';
    printf("%c\n", ft_toupper(c1));
    printf("%c\n", toupper(c1));

ft_strchr

strrchr
    char *s1 = "abcdefghijklmnoparstuvwxyz";
    char *p1;

    p1 = strrchr(s1, 'a');
    printf("A palavra ficou %s. \n", p1);

    char *s2 = "abcdefghijklmnoparstuvwxyz";
    char *p2;

    p2 = strrchr(s2, 'a');
    printf("A palavra ficou %s. \n", p2);


ft_strncmp

	char s1[] = "abcdefghijklm/&*nop21arstuvwxyz";
	char *p1;
	char s2[] = "abcdefghijklm/&*nop21arstuvwxyz";
	char *p2;

	p1 = ft_memchr(s1, '/', strlen(s1));
	printf("A palavra ficou %s. \n", p1);
	p2 = memchr(s2, '/', strlen(s2));
	printf("A palavra ficou %s. \n", p2);


ft_memcmp
	char s1[] = "Hello World";
	int p1;
	char s2[] = "Hello World";
	int p2;

	p1 = ft_memcmp(s1, s2, 10);
	p2 = memcmp(s1, s2, 10);
	printf("\n-----------------------//-----------------------\n");
	printf("A minha versao deu: %d, e a versao correta deu: %d. \n", p1, p2);
	printf("-----------------------//-----------------------\n\n");


ft_atoi(usa argc e argv)
	if (ac)
		printf("%i", ft_atoi(av[1]));


ft_strnstr
	char s1[] = "Hello World 123456789";
	char *p1;

	p1 = ft_strnstr(s1, "1", 13);
	printf("A palavra ficou %s. \n", p1);


ft_calloc
	char *string1_calloc;

	string1_calloc = ft_calloc(10, 1);
	printf("The newly created function is %s.\n", string1_calloc);
	free(string1_calloc);


ft_strdup
	char *s1_strdup = "Hello World";
	char *s2_strdup;

	s2_strdup = ft_strdup(s1_strdup);
	printf("The newly created function is %s.\n", s2_strdup);
	free(s2_strdup);
*/
