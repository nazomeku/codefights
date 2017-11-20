"""Sum of all the prime numbers in the range (a, b)."""

def primes_sum(a, b):
    return sum([x for x in range(a, b+1) if x >= 2 and not any([x%y == 0 for y in range(2, int(x**0.5) + 1)])])
