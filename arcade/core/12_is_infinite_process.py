"""Given integers a and b, determine whether the following pseudocode results
in an infinite loop
while a is not equal to b do
  increase a by 1
  decrease b by 1
"""


def is_infinite_process(a, b):
    return a > b or (b-a) % 2
