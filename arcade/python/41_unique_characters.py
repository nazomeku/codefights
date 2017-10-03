"""Given a document, return an array of all unique characters that appear in
it sorted by their ASCII codes."""


def unique_characters(document):
    return sorted(set(document))
