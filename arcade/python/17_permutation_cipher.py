"""Given the password you always use, your task is to encrypt it using the
permutation cipher with the given key."""


def permutation_cipher(password, key):
    table = str.maketrans("abcdefghijklmnopqrstuvwxyz", key)
    return password.translate(table)
