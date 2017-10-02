"""Given this data, return a list representing a horizontal histogram, where
each bar is formed by the given character ch."""


def create_histogram(ch, data):
    return list(map(lambda x: x*ch, data))
