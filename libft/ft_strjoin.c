#include "libft.h"

char *ft_strjoin(char const *s1, char const *s2)
{
	char	*sum;
	int	s1_size;
	int	s2_size;

	s1_size = (unsigned int)ft_strlen((char *)s1);
	s2_size = (unsigned int)ft_strlen((char *)s2);
	if (s1_size == 0 || s2_size == 0)
		return strdup("");
	sum = (char *)malloc(sizeof(char) * (s1_size + s2_size + 1));
	if (!sum)
		return (NULL);
	ft_strlcpy(sum, s1, s1_size + 1);
	ft_strlcpy(sum + s1_size, s2, s2_size + 1);

	return (sum);
}
