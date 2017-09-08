"""Your task is to calculate the difference between the sums of numbers written
 on the backs of the students that will join team A, and those written on the
 backs of the students that will join team B."""


def two_teams(students):
    return sum(students[::2]) - sum(students[1::2])
