"""Given a list of athletes, return the list of athletes after the
changes, i.e. after each adjacent pair of athletes is swapped."""


def correct_lineup(athletes):
    return [athletes[i^1] for i in range(len(athletes))]
