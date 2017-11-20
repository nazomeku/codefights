"""Given a list of attempts and the correct password, return the 1-based
index of the first correct attempt, or -1 if there were none."""


def check_password(attempts, password):
    def check():
        while True:
            helper = yield
            yield helper == password

    checker = check()
    for i, attempt in enumerate(attempts):
        next(checker)
        if checker.send(attempt):
            return i + 1

    return -1
