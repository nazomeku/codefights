"""What is the total maximum value of the items you can take with you,
assuming that your max weight capacity is maxW and you can't come back for
the items later?"""


def knapsack_light(value1, weight1, value2, weight2, max_w):
    if weight1 + weight2 <= max_w:
        return value1 + value2
    elif weight1 <= max_w and weight2 <= max_w:
        return max(value1, value2)
    elif weight1 <= max_w and weight2 > max_w:
        return value1
    elif weight1 > max_w and weight2 <= max_w:
        return value2
    else:
        return 0
