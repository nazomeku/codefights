"""Given the pressures Harry wrote down for each pipe, return two lists: the
first one containing the minimum, and the second one containing the maximum
pressure of each pipe during the day."""


def pressure_gauges(morning, evening):
    return list(map(min, morning, evening)), list(map(max, morning, evening))
