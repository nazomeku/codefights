"""Given an array of integers, write a function that determines whether the
array contains any duplicates."""


def contains_duplicates(a):
    return len(set(a)) != len(a)
