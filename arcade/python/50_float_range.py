"""Return a list of values from start to stop (including start and not
including stop), evenly spaced by the step."""
from itertools import takewhile, count


def float_range(start, stop, step):
    gen = takewhile(lambda x: x < stop, count(start, step))
    return list(gen)
