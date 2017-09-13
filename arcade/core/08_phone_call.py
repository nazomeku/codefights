"""You have s cents on your account before the call. What is the duration 
of the longest call (in minutes rounded down to the nearest integer)
you can have?"""


def phone_call(min1, min2_10, min11, s):
    total = 0
    if s >= min1:
        s -= min1
        total += 1
    while s >= min2_10 and total < 10:
        s -= min2_10
        total += 1
    while s >= min11 and total >= 10:
        s -= min11
        total += 1
        print(str(s) + ' ' + str(total))
    return total
