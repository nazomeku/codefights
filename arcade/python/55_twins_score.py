"""Given two lists of equal size representing the scores Billy and Mandy got
for each exam (b and m, respectively), return a single list containing their
combined score."""


def twins_score(b, m):
    return list(map(sum, zip(b, m)))
