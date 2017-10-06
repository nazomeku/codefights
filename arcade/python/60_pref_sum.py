"""Given array a, your task is to calculate all its prefix sums."""
from itertools import accumulate


def pref_sum(a):
    return list(accumulate(a))
