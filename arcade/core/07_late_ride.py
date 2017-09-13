"""Return an answer as the sum of digits that the digital timer in the format
hh:mm would show."""


def late_ride(n):
    hours = n // 60
    minutes = n - (hours*60)
    total = str(hours) + str(minutes)
    return sum(map(int, total))
