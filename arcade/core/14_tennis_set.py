"""Determine if it is possible for a tennis set to be finished with
the score score1 : score2."""


def tennis_set(score1, score2):
    if max(score1, score2) == 6 and min(score1, score2) < 5:
        return True
    elif min(score1, score2) in (5, 6) and max(score1, score2) == 7:
        return True
    else:
        return False
