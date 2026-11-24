# include "../codexion.h"


int	ft_atoi(const char *str);
int	ft_strlen(const char *str);

int	ft_strlen(const char *str)
{
	int	n;

	n = 0;
	while (str[n] != '\0')
	{
		n++;
	}
	return (n);
}
