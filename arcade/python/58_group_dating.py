"""When a male and a female cat with the same nature value see each
other, they become connected and happily walk out together."""


def group_dating(male, female):
    return [[x for x, y in zip(male, female) if x != y], [y for x, y in zip(male, female) if x != y]]
