"""Write a function that, given an array ofintegers arr, sorts its elements
in ascending order."""


def simple_sort(arr):
    n = len(arr)
    for i in range(n):
        j = 0
        stop = n - i
        while j < stop - 1:
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            j += 1
    return arr
