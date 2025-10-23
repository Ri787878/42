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
	char	*src;
	char	*dest1;
	char	*dest2;

	src = "BOM dia !!";
	dest1 = NULL;
	dest2 = NULL;
	dest1 = malloc(10 * sizeof(char));
	dest2 = malloc(10 * sizeof(char));
	printf("String:\t%s\n", src);
	ft_memmove(dest1, src, 10);
	printf("My version:\t%s\n", dest1);
	memmove(dest2, src, 10);
	printf("Original:\t%s\n", dest2);
	free(dest1);
	free(dest2);
	return (0);
}

// strlcpy
int	main(void)
{
	char	*test;
	char	result[27];
	size_t	code;

	test = "abcdefghijklmnopqrstuvwxyz";
	code = ft_strlcpy(result, test, 27);
	printf("the exit code is %lu\n", code);
	printf("The word\t\"%s\"\n result is \t\"%s\".\n", test, result);
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
	char	*src;
	char	dst[30];
	int		n;
	size_t	code;

	src = "abcdefghijklmnopqrstuvwxyz";
	n = 0;
	while (n <= 10)
	{
		dst[n] = 'X';
		n++;
	}
	dst[n] = '\0';
	printf("dst = %s\n", dst);
	code = ft_strlcat(dst, src, 34);
	printf("the exit code is %lu\n", code);
	printf("The word\t\"%s\"\n result is \t\"%s\".\n", src, dst);
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
		result = ft_strncmp(tests[n], tests[0], 5);
		result_true = strncmp(tests[n], tests[0], 5);
		printf("\nThe frase \"%s\"\n", tests[n]);
		printf("MINE result is \t\"%d\"\n", result);
		printf("THEI result is \t\"%d\"\n", result_true);
		n++;
	}
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
