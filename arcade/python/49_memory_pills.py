"""Return a list of three names that go right after the very first medicine
name of the even length."""
from itertools import dropwhile


def memory_pills(pills):
    gen = dropwhile(lambda x: len(x) % 2, pills + [''] * 3)
    next(gen)
    return [next(gen) for _ in range(3)]
