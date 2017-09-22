"""Given result, return an array of the same length, where the ith element is
equal to the ith element of result with the last digit dropped."""


def fix_result(result):
    def fix(x):
        return x // 10
    return list(map(fix, result))
