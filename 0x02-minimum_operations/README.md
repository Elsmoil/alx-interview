 """
    Calculates the minimum number of operations to get exactly n 'H' characters
    using only the 'Copy All' and 'Paste' operations.

    The algorithm works by performing prime factorization on the input number n.
    Each prime factor contributes a number of operations equal to its value.
    For example, to create 12 characters, the prime factors are 2 and 3, and the total
    operations are the sum of these factors.

