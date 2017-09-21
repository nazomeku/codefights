"""Given an integer n, return a shell list."""


def construct_shell(n):
    return [[0] * (i + 1 if i < n else 2 * n - i - 1) for i in range(n * 2 - 1)]
