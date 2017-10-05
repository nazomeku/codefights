"""Given the list of numbers, return the kth (1-based) permutation that
you should begin with."""
from itertools import permutations


def kth_permutation(numbers, k):
    return list(permutations(numbers, len(numbers)))[k-1]
