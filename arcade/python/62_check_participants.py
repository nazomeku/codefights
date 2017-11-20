"""Given the list of participants, your task is to return the list of
games for which too few people signed up."""


def check_participants(participants):
    return [a for a, b in enumerate(participants) if a > b]
