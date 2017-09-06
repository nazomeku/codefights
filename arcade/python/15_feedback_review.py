"""Implement a function that, given a feedback and the size of the screen,
splits the feedback into lines."""
import textwrap


def feedback_review(feedback, size):
    return textwrap.wrap(feedback, size)
