"""You would like to write a function that takes integer numbers x, y, L and R
as parameters and returns True if xy lies in the interval (L, R] and False
otherwise. You're considering several ways to write a conditional statement
inside this function:
What option would be the most efficient in terms of execution time?
"""

# if L < x ** y <= R:
# if x ** y > L and x ** y <= R:
# if x ** y in range(L + 1, R + 1):

print("if x ** y in range(L + 1, R + 1):")
