"""Given the list of the players and the number of players k the coach has
to pick, return all possible lineups sorted lexicographically. Players in each
lineup should also be sorted lexicographically."""
from itertools import combinations


def crazyball(players, k):
    return list(combinations(sorted(players), k))
