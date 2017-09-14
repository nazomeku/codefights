"""Given values experience, threshold and reward, check if you reach the next
level after killing the monster."""


def reach_next_level(experience, threshold, reward):
    if experience + reward >= threshold:
        return True
    else:
        return False
