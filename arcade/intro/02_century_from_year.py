"""Given a year, return the century it is in."""


def century_from_year(year):
    if year % 100 == 0:
        return year // 100
    return (year // 100) + 1
