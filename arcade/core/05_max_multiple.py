"""Given a divisor and a bound, find the largest integer N such that:
N is divisible by divisor.
N is less than or equal to bound.
N is greater than 0."""


def max_multiple(divisor, bound):
    return int(bound/divisor) * divisor
