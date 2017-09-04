"""You are given a two-digit integer n. Return the sum of its digits."""


def add_two_digits(n):
    z = [x for x in str(n)]
    return int(z[0]) + int(z[1])

