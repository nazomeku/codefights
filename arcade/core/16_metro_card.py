"""Figure out the number of days by which your pass will now be extended, and
return all the options as an array sorted in increasing order."""


def metro_card(days):
    return [28, 30, 31] if days == 31 else [31]
