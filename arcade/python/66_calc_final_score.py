"""Given the list of scores the player got for completed levels and the
number n that determines the number of levels you have to pass to avoid
being penalized, return the player's final game score."""


def calc_final_score(scores, n):
    gen = (x**2 for x in sorted(scores, reverse=True))

    res = 0
    try:
        for _ in range(n):
            res += next(gen)
    except StopIteration:
        res //= 5

    return res
