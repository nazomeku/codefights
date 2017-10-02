"""For the given list of denominators, find the least common denominator by
finding their LCM."""
from math import gcd
from functools import reduce


def least_common_denominator(denominators):
    return reduce(lambda x, y: x * y // gcd(x, y), denominators)
