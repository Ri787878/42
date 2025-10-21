NAME = libft.a

SOURCEDIR = srcs
INCLUDES = includes

SRCS := $(shell find $(SOURCEDIR) -name '*.c')
OBJECTS = $(SRCS:.c=.o)

CC = cc
CFLAGS = -Wall -Wextra -Werror -I$(INCLUDES)

AR = ar rcs
RM = rm -f

all: $(NAME)

$(NAME): $(OBJECTS)
	$(AR) $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	$(RM) $(OBJECTS)

fclean: clean
	$(RM) $(NAME)

re: fclean all

.PHONY: all clean fclean re

