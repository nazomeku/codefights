"""Given an integer n, return the multiplication table of size n × n."""


def multiplication_table(n):
    return [[i*j for i in range(1, n + 1)] for j in range(1, n + 1)]
