"""To repair the damage, you need to start with implementing a function that
will replace all multiple space characters in the given line of your code
with single ones. In addition, all leading and trailing whitespaces should be
removed."""


def cat_walk(code):
    return " ".join(code.split())
