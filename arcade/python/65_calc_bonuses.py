"""Given the bonuses the player got, your task is to return his final
score for the level."""


def calc_bonuses(bonuses, n):
    it = (x for x in bonuses)
    res = 0

    try:
        for _ in range(n):
            res += next(it)
    except StopIteration:
        res = 0

    return res
