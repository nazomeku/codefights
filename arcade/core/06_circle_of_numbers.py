"""Given n and first_number, find the number which is written in the radially
opposite position to first_number."""


def circle_of_numbers(n, first_number):
    if first_number < n/2:
        return first_number + n/2
    else:
        return first_number - n/2
