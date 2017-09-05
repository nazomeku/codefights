"""Implement a function that, given an integer number n and a base x,
converts n from base x to base 16."""


def base_conversion(n, x):
    return hex(int(n, x))[2:]
