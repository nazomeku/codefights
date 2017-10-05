"""Given the list of the players, your task is to come up with the list of
all the games between them, and return them sorted lexicographically."""
from itertools import permutations


def rock_paper_scissors(players):
    return sorted(permutations(players, 2))
