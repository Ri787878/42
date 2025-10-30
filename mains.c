/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   mains.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ridias <ridias@student.42.fr>              +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/10/24 13:16:21 by ridias            #+#    #+#             */
/*   Updated: 2025/10/30 16:24:38 by ridias           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

// ft_memcpy
int	main(void)
{
	char	src[10] = "BOM dia !!";
	char	dest1[10];
	char	dest2[10];

	printf("String:\t%s\n", src);
	ft_memcpy(dest1, src, 10);
	printf("My version:\t%s\n", dest1);
	memcpy(dest2, src, 10);
	printf("Original:\t%s\n", dest2);
	return (0);
}

// ft_isalpha
int	main(void)
{
	int		n;
	char	src[13] = "BOM dia 123!!";

	n = 0;
	printf("String:\t%s\n", src);
	while (n < sizeof(src))
	{
		printf("letter %c is %d\n", src[n], ft_isalpha(src[n]));
		n++;
	}
	return (0);
}

// isdigit
int	main(void)
{
	int		n;
	char	src[13] = "BOM dia 123!!";

	n = 0;
	printf("String:\t%s\n", src);
	while (n < sizeof(src))
	{
		printf("letter %c is %d\n", src[n], ft_isdigit(src[n]));
		n++;
	}
	return (0);
}

// isalnum
int	main(void)
{
	unsigned long	n;
	char			src[13] = "BOM dia 1\n3!!";

	n = 0;
	printf("String:\t%s\n", src);
	while (n < sizeof(src))
	{
		printf("letter %c is %d\n", src[n], ft_isalnum(src[n]));
		n++;
	}
	return (0);
}

// ft_isascii
int	main(void)
{
	unsigned long	n;
	char			src[13] = "BOM dia 1\n3!!";

	n = 0;
	printf("String:\t%s\n", src);
	while (n < sizeof(src))
	{
		printf("letter %c is %d\n", src[n], ft_isascii(src[n]));
		n++;
	}
	return (0);
}

// ft_isprint
int	main(void)
{
	unsigned long	n;
	char			src[13] = "BOM dia \t\n3!!";

	n = 0;
	printf("String:\t%s\n", src);
	while (n < sizeof(src))
	{
		printf("letter %c is %d\n", src[n], ft_isprint(src[n]));
		n++;
	}
	return (0);
}

// strlen
int	main(void)
{
	char	src[10] = "BOM dia !!";

	printf("String:\t\"%s\"\n", src);
	printf("My version:\t%lu\n", ft_strlen(src));
	printf("Original:\t%lu\n", strlen(src));
	return (0);
}

// ft_bzero
int	main(void)
{
	char	*src;

	src = "BOM dia !!";
	printf("String:\t%s\n", src);
	ft_bzero(src, 10);
	printf("My version:\t%s\n", src);
	return (0);
}

// memmove
int	main(void)
{
	char	src[] = "consectetur";
	char	dest1[] = "ipsum dolor sit a";
	char	dest2[] = "ipsum dolor sit a";

	printf("String:\t%s\n", src);
	memmove(dest2, src, 5);
	printf("Original:\t\"%s\"\n", dest2);
	ft_memmove(dest1, src, 5);
	printf("My version:\t\"%s\"\n", dest1);

	return (0);
}

// strlcpy
int	main(void)
{
	char	test1[] = "abcdefghijklmnopqrstuvwxyz";
	char	test2[] = "abcdefghijklmnopqrstuvwxyz";
	char	result1[27];
	char	result2[27];
	size_t	size;

	size = ft_strlcpy(result1, test1, 27);
	printf("the exit size is %lu\n", size);
	printf("The word\t\"%s\"\n result is \t\"%s\".\n", test1, result1);

	size = strlcpy(result2, test2, 27);
	printf("the exit size is %lu\n", size);
	printf("The word\t\"%s\"\n result is \t\"%s\".\n", test2, result2);
	return (0);
}

int	main(void)
{
	char	tests[4][27] = {"abcdefghijklmnopqrstuvwxyz", "Maria is nice!!",
			"0123456789", "the \t tab is tabb\ting"};
	char	result[27];
	int		n;
	int		size;

	n = 0;
	size = 4;
	// int		t = 0;
	while (n < size)
	{
		ft_strlcpy(result, tests[n], ft_strlen(tests[n]) + 1);
		printf("The word\t\"%s\"\n result is \t\"%s\"\n\n", tests[n], result);
		n++;
	}
	return (0);
}

// strlcat
int	main(void)
{
	char	src1 = 'a';
	char	src2 = 'a';
	char	dst1[30];
	char	dst2[30];
	int		n;
	size_t	code;

	n = 0;
	while (n <= 10)
	{
		dst1[n] = 'X';
		dst2[n] = 'X';
		n++;
	}
	dst1[n] = '\0';
	dst2[n] = '\0';
	printf("dst1 = %s\n", dst1);
	code = strlcat(dst1, src1, 30);
	printf("the exit code is %lu\n", code);
	printf(" Original\t\"%s\"\n result is \t\"%s\".\n", src1, dst1);


	printf("dst2 = %s\n", dst2);
	code = ft_strlcat(dst2, src2, 30);
	printf("the exit code is %lu\n", code);
	printf("Mine\t\t\"%s\"\n result is \t\"%s\".\n", src2, dst2);
	return (0);
}

// toupper && tolower
int	main(void)
{
	int		n;
	char	str[] = "abcdefGHIJK012345n\tcc";

	n = 0;
	printf("before:\t%s\n", str);
	while (str[n] != '\0')
	{
		str[n] = (char)ft_toupper(str[n]);
		n++;
	}
	printf("after:\t%s\n", str);
	return (0);
}
int	main(void)
{
	int		n;
	char	str[] = "abcdefGHIJK012345n\tCC";

	n = 0;
	printf("before:\t%s\n", str);
	while (str[n] != '\0')
	{
		str[n] = (char)ft_tolower(str[n]);
		n++;
	}
	printf("after:\t%s\n", str);
	return (0);
}

// strchr
int	main(void)
{
	char	tests[4][27] = {"abcdefghijklmnopqrstuvwxyz", "Maria is nice!!",
			"0123456789", "the \t tab is tabb\ting"};
	char	*result_true;
	char	*result;
	int		n;
	int		size;

	n = 0;
	size = 4;
	while (n < size)
	{
		result = ft_strchr(tests[n], 'i');
		result_true = strchr(tests[n], 'i');
		printf("\nThe frase \"%s\"\n", tests[n]);
		printf("MINE result is \t\"%s\"\n", result);
		printf("THEI result is \t\"%s\"\n", result_true);
		n++;
	}
	return (0);
}

// strrchr
int	main(void)
{
	char	tests[4][27] = {"abcdefghijklmnopqrstuvwxyz", "Maria is nice!!",
			"0123456789", "the \t tab is tabb\ting"};
	char	*result_true;
	char	*result;
	int		n;
	int		size;

	n = 0;
	size = 4;
	while (n < size)
	{
		result = ft_strrchr(tests[n], 'i');
		result_true = strrchr(tests[n], 'i');
		printf("\nThe frase \"%s\"\n", tests[n]);
		printf("MINE result is \t\"%s\"\n", result);
		printf("THEI result is \t\"%s\"\n", result_true);
		n++;
	}
	return (0);
}

// strncmp
int	main(void)
{
	int		result_true;
	int		result;

	result = ft_strncmp("test\200", "test\0", 6);
	result_true = strncmp("test\200", "test\0", 6);
	printf("\nThe frase \"%s\" && \"%s\"\n", "test\200", "test\0");
	printf("MINE result is \t\"%d\"\n", result);
	printf("THEI result is \t\"%d\"\n", result_true);
	return (0);
}

// memchr
int	main(void)
{
	char	tests[4][27] = {"abcdefghijklmnopqrstuvwxyz", "Maria is nice!!",
			"0123456789", "the \t tab is tabb\ting"};
	char	*result_true;
	char	*result;
	int		n;
	int		size;

	n = 0;
	size = 4;
	while (n < size)
	{
		result = ft_memchr(tests[n], 'i', 20);
		result_true = memchr(tests[n], 'i', 20);
		printf("\nThe frase \"%s\"\n", tests[n]);
		printf("MINE result is \t\"%s\"\n", result);
		printf("THEI result is \t\"%s\"\n", result_true);
		n++;
	}
	return (0);
}

// memcmp
int	main(void)
{
	char	tests[4][27] = {"abcdefghijklmnopqrstuvwxyz", "Maria is nice!!",
			"0123456789", "the \t tab is tabb\ting"};
	int		result_true;
	int		result;
	int		n;
	int		size;

	n = 0;
	size = 4;
	while (n < size)
	{
		result = ft_memcmp(tests[n], tests[0], 5);
		result_true = memcmp(tests[n], tests[0], 5);
		printf("\nThe frase \"%s\" && comparing \"%s\"\n", tests[n], tests[0]);
		printf("MINE result is \t\"%d\"\n", result);
		printf("THEI result is \t\"%d\"\n", result_true);
		n++;
	}
	return (0);
}

// strnstr
int	main(void)
{
	char	tests[4][27] = {"abcdefghijklmnopqrstuvwxyz", "Maria is nice!!",
			"0123456789", "the \t tab is tabb\ting"};
	char	*result;
	int		n;
	int		size;

	n = 0;
	size = 4;
	while (n < size)
	{
		result = ft_strnstr(tests[n], "b", strlen(tests[n]));
		printf("\nThe frase \"%s\"\n", tests[n]);
		printf("MINE result is \t\"%s\"\n", result);
		n++;
	}
	return (0);
}

// atoi
int	main(void)
{
	char	*tests[] = {"42", "   42", "-42", "+42", "0042", "123abc", "abc123",
			"--5", "", "  + 5", "2147483647", "-2147483648", NULL};
	int		i;
	int		mine;
	int		real;

	i = 0;
	while (tests[i])
	{
		mine = ft_atoi(tests[i]);
		real = atoi(tests[i]);
		printf("Test %2d: \"%s\"\n", i + 1, tests[i]);
		printf("ft_atoi: %d\tatoi: %d\n\n", mine, real);
		i++;
	}
	return (0);
}

//calloc
int	main(void)
{
	int	*a;
	int	*b;
	int	i;

	i = 0;
	a = ft_calloc(10, sizeof(int));
	b = calloc(10, sizeof(int));
	while (i < 10)
	{
		printf("ft_calloc[%d] = %d\t\t| calloc[%d] = %d\n", i, a[i], i, b[i]);
		i++;
	}
	free(a);
	free(b);
}

//substr
size_t	ft_strlen(const char *str)
{
	int	n;

	n = 0;
	while (str[n] != '\0')
	{
		n++;
	}
	return (n);
}

int	main(void)
{
	char	tests[4][27] = {"abcdefghijklmnopqrstuvwxyz", "Maria is nice!!",
		"0123456789", "the \t tab is tabb\ting"};
	char	*result;
	int		n;
	int		size;

	n = 0;
	size = 4;
	while (n < size)
	{
		result = ft_substr(tests[n], 5, ft_strlen(tests[n]));
		printf("\nThe frase \"%s\"\n", tests[n]);
		printf("MINE result is \t\"%s\"\n", result);
		free(result);
		n++;
	}
	return (0);
}

//strjoin

int	main(void)
{
	char	tests[5][27] = {"abcdefghijklmnopqrstuvwxyz", "Maria is nice!!",
		"0123456789", "the \t tab is tabb\ting", ""};
	char	*result;
	int		n;
	int		t;
	int		size;

	n = 0;
	size = 5;
	t = size - 1;
	while (n < size)
	{
		result = ft_strjoin(tests[n], tests[t]);
		printf("\nThe 1st frase \"%s\"\nThe 2nd frase \"%s\"\n", tests[n], tests[t]);
		printf("MINE result is \t\"%s\"\n", result);
		free(result);
		t--;
		n++;
	}
	return (0);
}

//strtrim
int	main(void)
{
	char	tests[5][27] = {"abcdefghijklmnopqrstuvwxyz", "Maria is nice!!",
		"0123456789", "the \t tab is tabb\ting", ""};
	char	*result;
	int		n;
	int		t;
	int		size;

	n = 0;
	size = 5;
	t = size - 1;
	while (n < size)
	{
		result = ft_strtrim(tests[n], "Mb anichret");
		printf("\nThe 1st frase \"%s\"\n", tests[n]);
		printf("MINE result is \t\"%s\"\n", result);
		t--;
		n++;
	}
	return (0);
}

//split
int	main(void)
{
	char	**result;
	char	separator;
	int		n;

	separator = ' ';
	n = 0;
	result = ft_split("Maria is nice!!", separator);
	while (n < 3)
	{
		printf("result[%d] = %s\n", n, result[n]);
		n++;
	}
	free(result);
	return (0);
}

//itoa
int	main(void)
{
	int		n;
	char	*nbr;

	n = -123456789;
	nbr = ft_itoa(n);
	printf("the number %d,", n);
	printf(" turns to the string %s\n", nbr);
	nbr = ft_itoa(0);
	n = 0;
	printf("the number %d,", n);
	printf(" turns to the string %s\n", nbr);
	nbr = ft_itoa(-1);
	n = -1;
	printf("the number %d,", n);
	printf(" turns to the string %s\n", nbr);
	nbr = ft_itoa(2147483647);
	n = 2147483647;
	printf("the number %d,", n);
	printf(" turns to the string %s\n", nbr);
	nbr = ft_itoa(-2147483648);
	n = -2147483648;
	printf("the number %d,", n);
	printf(" turns to the string %s\n", nbr);
	free(nbr);
	return (0);
}

//strmapi
char to_upper(unsigned int i, char c) {
	(void)i;  // ignore the index
	if (c >= 'a' && c <= 'z')
		return c - ('a' - 'A');
	return c;
}

int	main(void)
{
	char	*string = "Maria is Nice!!";
	char	*result;

	result = malloc(ft_strlen(string));
	printf("The string: \"%s\", ", string);
	result = ft_strmapi(string, to_upper);
	printf("turns to become: \"%s\"\n", result);
	free(result);
	return(0);
}

//striteri
void	to_upper(unsigned int i, char *c)
{
	(void)i;
	if (*c >= 'a' && *c <= 'z')
		*c = *c - 32;
}

int	main(void)
{
	char	string[] = "Maria is Nice!!";

	printf("The string: \"%s\", ", string);
	ft_striteri(string, to_upper);
	printf("turns to become: \"%s\"\n", string);
	return (0);
}

//putchar_fd
int	main(void)
{
	ft_putchar_fd('a', 1);
	ft_putchar_fd('\n', 1);
	ft_putchar_fd('c', 1);
	ft_putchar_fd('\n', 1);
	ft_putchar_fd('\t', 1);
	ft_putchar_fd('g', 1);
	return (0);
}

//putstr_fd
int	main(void)
{
	char	string[] = "Maria is Nice!!";

	ft_putstr_fd(string, 1);
	return (0);
}

//putendl_fd
int	main(void)
{
	char	string[] = "Maria is Nice!!";

	ft_putendl_fd(string, 1);
	return (0);
}

//ft_putnbr_fd
int	main(void)
{
	ft_putnbr_fd(123456789, 1);
	return (0);
}
