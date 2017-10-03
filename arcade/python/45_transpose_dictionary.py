""" As a starting point, you'd like to obtain the (extension, script) pairs
from the dictionary, sorted lexicographically by the extensions."""


def transpose_dictionary(script_by_extension):
    return sorted([(v, k) for k, v in script_by_extension.items()])
