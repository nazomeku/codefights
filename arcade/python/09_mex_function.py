"""For the given set s and given an upper_bound, implement a function that will
find its mex if it's smaller than upper_bound or return upperBound instead."""


def mex_function(s, upper_bound):
    found = -1
    for i in range(upper_bound):
        if not i in s:
            found = i
            break
    else:
        found = upper_bound
    return found
