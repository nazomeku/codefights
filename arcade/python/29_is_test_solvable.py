"""Given the list of question ids, determine if the sum of their digits is
divisible by k to see if it's worth trying to pass the test."""


def is_test_solvable(ids, k):
    digit_sum = lambda x: sum(map(int, str(x)))
    temp = 0
    for question_id in ids:
        temp += digit_sum(question_id)
    return temp % k == 0
