"""Given an integer n, return a list of n lists, where the first element
consists is empty (consists of 0 zeros), the second element consists
of 1 zero, and so on."""
from functools import reduce


def fibonacci_list(n):
    return [[0] * x for x in reduce(lambda x, y: x + [x[y] + x[y - 1]], range(1, n-1), [0, 1])]
