"""Given a rational number, your task is to return its 0-based index
in the Calkin-Wilf sequence."""


def calkin_wilf_sequence(number):
    def fractions():
        n, d = 0, 1
        while True:
            n, d = d, 2 * (n // d) * d + d - n
            yield list((n, d))

    gen = fractions()
    res = 0
    while next(gen) != number:
        res += 1
    return res
