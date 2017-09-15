"""Knowing whether a person is young, beautiful and loved, find out if they
contradict Mary's belief."""


def will_you(young, beautiful, loved):
    if young and beautiful and not loved:
        return True
    elif loved and not (young and beautiful):
        return True
    else:
        return False
