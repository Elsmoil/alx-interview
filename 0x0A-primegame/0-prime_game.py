#!/usr/bin/python3
    """
This module contains functions to simulate a game between two players, Maria and Ben.
The game involves picking primes from a set of integers and removing them and their multiples.
The player who cannot make a valid move loses the game.
    """


def sieve_of_eratosthenes(n):
    """
    Returns a list of prime numbers up to n using the Sieve of Eratosthenes algorithm.

    Args:
        n (int): The upper limit (inclusive) to find primes.

    Returns:
        list: A list of prime numbers from 2 to n.

    Example:
        >>> sieve_of_eratosthenes(10)
        [2, 3, 5, 7]
    """
    if not isinstance(n, int) or n <= 1:
        raise ValueError("Input must be an integer greater than 1")

    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]


def isWinner(x, nums):
    """
    Determines the winner of multiple rounds of a prime-based game between two players, Maria and Ben.

    In each round, players take turns picking prime numbers from a set {1, 2, ..., n},
    and remove the chosen prime and its multiples. The player who cannot make a valid move loses.

    Maria always starts first and both players play optimally.

    Args:
        x (int): The number of rounds to simulate.
        nums (list): A list of integers n representing the upper limit for each round.

    Returns:
        str or None: The name of the player who won the most rounds ("Maria" or "Ben").
                     If the result is a tie, return None.

    Example:
        >>> isWinner(3, [4, 5, 1])
        "Ben"
    """
    if not isinstance(x, int) or x <= 0:
        raise ValueError("x must be a positive integer.")

    if not all(isinstance(n, int) and n >
               0 for n in nums):  # Allow 1 in the validation
        raise ValueError(
            "All numbers in nums must be integers greater than 0.")

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            # If n is 1, Ben automatically wins (no primes to pick)
            ben_wins += 1
            continue

        primes = sieve_of_eratosthenes(n)
        current_set = set(range(1, n + 1))
        turn = 0  # Maria starts first (0: Maria, 1: Ben)

        while primes:
            current_prime = primes.pop(0)
            current_set -= set(range(current_prime, n + 1, current_prime))
            primes = [p for p in primes if p <= n and p in current_set]
            turn = 1 - turn

        if turn == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
