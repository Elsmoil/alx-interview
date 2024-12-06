#!/usr/bin/python3
"""
    Calculates the minimum number of operations to get
    exactly n 'H' characters
    using only the 'Copy All' and 'Paste' operations.

    The algorithm works by performing prime factorization
    on the input number n.
    Each prime factor contributes a number of operations equal to its value
    For example, to create 12 characters,
    the prime factors are 2 and 3, and the total
    operations are the sum of these factors.
    """


def minOperations(n):
    """
    Calculates the minimum number of operations to get exactly n 'H' characters
    using only 'Copy All' and 'Paste' operations.

    Args:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations, or 0 if it's not possible.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    # Factor n and sum the operations for each prime factor
    while divisor * divisor <= n:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    # If n is still greater than 1, it is prime, add it as an operation
    if n > 1:
        operations += n

    return operations
