"""Implement a function that, given a list of numbers, will return the
result of the operation."""
from functools import reduce


def math_practice(numbers):
    return reduce(lambda a, b: a + b[1] if b[0] % 2 else a * b[1], enumerate(numbers), 1)
