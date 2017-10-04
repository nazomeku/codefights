"""Given the name of your company, return the prefix of the corresponding
cyclic string containing n characters."""
from itertools import cycle


def cyclic_name(name, n):
    gen = cycle(name)
    res = [next(gen) for _ in range(n)]
    return ''.join(res)
