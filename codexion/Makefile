NAME = codexion.a

CC = cc
CFLAGS = -Wall -Wextra -Werror
AR = ar rcs
RM = rm -f

SRCS =	src/codexion.c \
		src/parcer/parcer.c \
		src/utils/utils_parcer.c \
		src/utils/utils_debug.c \
		src/utils/utils_declare.c

TEST_SRCS = tester/tester.c \
            src/parcer/parcer.c \
			src/utils/utils_parcer.c \
			src/utils/utils_debug.c \
			src/utils/utils_declare.c


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

run: $(NAME)
	$(CC) -w -o codexion $(NAME)
	./codexion

clean:
	$(RM) $(OBJECTS) $(TEST_OBJECTS)

fclean: clean
	$(RM) $(NAME) tester_exec codexion

re: fclean all

.PHONY: all clean fclean re codexion run tester test

