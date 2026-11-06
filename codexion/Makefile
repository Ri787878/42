NAME = codexion.a

CC = cc
CFLAGS = -Wall -Wextra -Werror
AR = ar rcs
RM = rm -f

SRCS =	src/codexion.c \
		src/parcer/parcer.c

TEST_SRCS = tester/tester.c \
            src/codexion.c \
            src/parcer/parcer.c

OBJECTS = $(SRCS:.c=.o)
TEST_OBJECTS = $(TEST_SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJECTS)
	$(AR) $(NAME) $(OBJECTS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

tester: $(TEST_OBJECTS)
	$(CC) -w -o tester_exec $(TEST_OBJECTS)

test: tester
	./tester_exec

clean:
	$(RM) $(OBJECTS) $(TEST_OBJECTS)

fclean: clean
	$(RM) $(NAME) tester_exec

re: fclean all

.PHONY: all clean fclean re codexion run tester test

