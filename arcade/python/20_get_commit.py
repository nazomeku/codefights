"""Given such commit, your task is go remove the username part from it and
return the second part as an answer."""


def get_commit(commit):
    return ''.join(i for i in commit if i not in '0?+!')
