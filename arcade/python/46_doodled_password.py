"""Given a list of digits as they are written in the clockwise order, find
all other combinations the password could possibly have."""
from collections import deque


def doodled_password(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda x, y: x.rotate(-y), res, range(n)), 0)
    return [list(d) for d in res]
