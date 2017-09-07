""" Given the time t, the width of the screen and the precision with which
the time should be displayed, return a string that should be shown on the
billboard."""


def competitive_eating(t, width, precision):
    return '{:{align}{w}.{p}f}'.format(t, align='^', w=width, p=precision)
