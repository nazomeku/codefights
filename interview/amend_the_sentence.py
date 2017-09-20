"""You have been given a string s, which is supposed to be a sentence. However,
 someone forgot to put spaces between the different words, and for some reason
 they capitalized the first letter of every word. Return the sentence after
 making the amendments."""
import re


def amend_the_sentence(s):
    return re.sub(r'(?<=\w)([A-Z])', r' \1', s).lower()
