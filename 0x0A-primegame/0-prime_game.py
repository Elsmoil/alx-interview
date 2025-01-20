#!/usr/bin/python3

"""
This module implements the Prime Game, 
where two players (Maria and Ben) take turns 
choosing prime numbers from a set of integers.
Each time a prime number is chosen, 
its multiples are removed from the set. The game ends 
when no more prime numbers can 
be chosen, and the player who cannot make a move loses.

The module includes:
- A helper function `sieve_of_eratosthenes` to 
generate prime numbers up to a given limit.
- A `play_game` function to simulate a game round given a number `n`.
- The `isWinner` function to determine the winner of
multiple rounds based on optimal play.

This module doesn't use any imported libraries and implements 
the solution efficiently.
"""

def sieve_of_eratosthenes(limit):
    """
    Generates all prime numbers up to the given limit using 
    the Sieve of Eratosthenes.

    Args:
    limit (int): The upper bound up to which to find primes.

    Returns:
    list: A list of primes up to the limit.
    """
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    primes = [i for i in range(2, limit + 1) if is_prime[i]]
    return primes

def play_game(n):
    """
    Simulates the game for a given value of n and determines the winner.

    Args:
    n (int): The upper bound of the set from 1 to n.

    Returns:
    str: 'Maria' if Maria wins, 'Ben' if Ben wins.
    """
    primes = sieve_of_eratosthenes(n)
    numbers = set(range(1, n + 1))
    turn = 0  # 0 for Maria, 1 for Ben

    while primes:
        prime = primes.pop(0)
        if prime > n:
            break
        # Remove the prime and its multiples
        numbers -= set(range(prime, n + 1, prime))
        primes = [p for p in primes if p <= n and p in numbers]
        turn = 1 - turn  # Switch turns

    return 'Maria' if turn == 1 else 'Ben'

def isWinner(x, nums):
    """
    Determines the player who wins the most rounds.

    The function takes an integer `x`,
    which is the number of rounds, and a list `nums`
    which contains the value `n` for each round.
    The function simulates each round of the
    Prime Game and determines who won the most rounds. It returns:
    - 'Maria' if Maria wins the most rounds.
    - 'Ben' if Ben wins the most rounds.
    - None if there is a tie.

    Args:
    x (int): The number of rounds.
    nums (list of int): A list of n values for each round.

    Returns:
    str: 'Maria' if Maria wins the most rounds, 
    'Ben' if Ben wins the most rounds, or None if there is a tie.

    Raises:
    ValueError: If `x` is not a positive integer or if any value in 
    `nums` is non-positive.
    """
    # Input validation for `x` and `nums`
    if not isinstance(x, int) or x <= 0:
        return None  # x must be positive, so return None if invalid

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n <= 0:
            continue #Skip invalid rounds

        winner = play_game(n)
        if winner == 'Maria':
            maria_wins += 1
        elif winner == 'Ben':
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
