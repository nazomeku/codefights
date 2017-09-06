"""Given a word, check whether it is a palindrome or not. A string is
considered to be a palindrome if it reads the same in both directions."""


def is_word_palindrome(word):
    return word == word[::-1]
