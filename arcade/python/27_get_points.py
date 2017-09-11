"""Your task is to calculate the number of points a student got for some test.
Implement a function that would calculate the number of points received for the
test based on the given list of answers."""


def get_points(answers, p):
    question_points = lambda i, ans: i+1 if ans else -p
    res = 0
    for i, ans in enumerate(answers):
        res += question_points(i, ans)
    return res
