"""Determine whether there is a pair of numbers, where one number is taken from
 a and the other from b, that can be added together to get a sum of v."""


def sum_of_two(a, b, v):
    b = set(b)
    return any(v - x in b for x in a)
