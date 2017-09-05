"""Given a list a, your task is to chop off its first and its last element
until it becomes beautiful. Implement a function that will make the given a
beautiful as described, and return the resulting list as an answer."""


def list_beautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        a_, *res, a = res
    return res
