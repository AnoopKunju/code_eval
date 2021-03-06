#!/usr/bin/env python3
# encoding: utf-8

"""
Number Operations

Challenge Description:

Alice has invented a new card game to play with Bob. Alice made a deck
of cards with random values between 1 and 52. Bob picks 5 cards. Then,
he has to rearrange the cards so that by utilizing the operations
plus, minus, or times, the value of the cards reach Alice's favorite
number, 42. More precisely, find operations such that ((((val1 op1
val2) op2 val3) op3 val4) op4 val5) = 42.

Help Bob by writing a program to determine whether it is possible to
reach 42 given 5 card values.

For example, Bob picks 5 cards out of the deck containing 60, 1, 3, 5,
and 20. Bob rearranges the cards and supplies four operations, so that
5 * 20 - 60 + 3 - 1 = 42.

Input Sample:

The input consists of five integers on a line, separated by
spaces. Each integer V is 0 <= V <= 52.

44 6 1 49 47
34 1 49 2 21
31 38 27 51 18

Output Sample:

For each test case print a line containing "YES" if it is possible to
reach the value 42 according to the rules of the game, or "NO"
otherwise.

NO
YES
NO

"""

import sys
import operator
import itertools

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

operations = [operator.add, operator.mul, operator.sub]

possible_operations = list(itertools.product(operations, repeat=4))


for test in test_cases:
    numbers = [int(i) for i in test.split()]
    permutations = itertools.permutations(numbers, 5)
    possible = 'NO'
    for n in permutations:
        for op in possible_operations:
            total = op[3](op[2](op[1](op[0](n[0], n[1]), n[2]), n[3]), n[4])
            if total == 42:
                possible = 'YES'
                break
    print(possible)
    



