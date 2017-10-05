"""Given the digits that comprise the password, its length k and the number
d by which it is divisible, return a sorted list of strings that should be
tried as passwords."""
from itertools import product


def cracking_password(digits, k, d):
    def createNumber(digs):
        return "".join(map(str, digs))

    return list(filter(lambda x: int(x) % d == 0, map(createNumber, product(sorted(digits), repeat = k))))
