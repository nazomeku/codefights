"""Implement a function that, given a piece of code and a positive integer x
will turn each tabulation character in code into x whitespace characters."""


def convert_tabs(code, x):
    return code.replace("\t", " " * x)

