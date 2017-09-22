"""Given two lists a and b, find cool pairs with the first number in the pair
from a, and the second one from b. Return the number of different sums of
elements in such pairs."""


def cool_pairs(a, b):
    unique_sums = {i + j for i in a for j in b if not (i * j) % (i + j)}
    return len(unique_sums)
