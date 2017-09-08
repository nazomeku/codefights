"""Given two lists lst1 and lst2, your task is to return a list formed by the
 elements of lst1 followed by the elements of lst2."""


def lists_concatenation(lst1, lst2):
    res = lst1
    res.extend(lst2)
    return res
