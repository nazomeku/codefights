"""Implement a function that will find the most frequent character in
the given encryptedText."""
from collections import Counter


def frequency_analysis(encrypted_text):
    return Counter(encrypted_text).most_common(1)[0][0]
