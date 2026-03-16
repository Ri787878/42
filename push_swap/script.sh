#!/bin/bash
make re
make clean

#clear

#echo "cc -Wall -Wextra -Werror push_swap.a -o push_swap"
cc -Wall -Wextra -Werror push_swap.a -o push_swap

ARG="14 -8 22 -3 5 -19 11 0 -24 17 -1 9 -15 25 -6 3 18 -21 7 -12 20 -4 13 -25 2 8 -9 16 -22 4 23 -14 10 -20 6 -2 19 -17 1 24 -5 15 -7 12 -23 21 -10 -18 -13 -11"
echo "valgrind  --leak-check=full ./push_swap \"$ARG\""
echo "Running push_swap with ARG..."

# ./push_swap $ARG
./push_swap $ARG | ./checker_linux $ARG
#valgrind  --leak-check=full ./push_swap $ARG

# Optional: Run just push_swap to see moves

