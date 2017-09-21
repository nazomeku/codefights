"""Given a word, calculate its "power"."""
import string


def word_power(word):
    num = dict(zip(string.ascii_lowercase, [i for i in range(1, 27)]))
    return sum([num[ch] for ch in word])

