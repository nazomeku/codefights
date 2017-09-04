"""Given an array of integers, find the pair of adjacent
elements that has the largest product and return that product."""


def adjacent_elements_product(arr):
    return max([arr[i] * arr[i+1] for i in range(len(arr)-1)])
