#!/usr/bin/python3
"""
This module contains functions to simulate a game between two players, Maria and Ben. 
The game involves picking primes from a set of integers and removing them and their multiples.
The player who cannot make a valid move loses the game.
"""

def sieve_of_eratosthenes(n):
     """
    This function uses the Sieve of Eratosthenes algorithm to find all
    prime numbers
    up to a given number `n`.

    Args:
        n (int): The upper limit (inclusive) to find primes.

    Returns:
        list: A list of prime numbers from 2 to `n`.

    Example:
        >>> sieve_of_eratosthenes(10)
        [2, 3, 5, 7]
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]

def isWinner(x, nums):
    """Returns the name of the player that won the most rounds."""
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = sieve_of_eratosthenes(n)
        current_set = set(range(1, n + 1))
        turn = 0  # Maria starts first (0: Maria, 1: Ben)
        
        while primes:
            # The current player picks the smallest prime
            current_prime = primes.pop(0)
            # Remove the prime and its multiples from the current set
            current_set -= set(range(current_prime, n + 1, current_prime))
            # Recompute the primes left in the current set
            primes = [p for p in primes if p <= n and p in current_set]
            
            # Alternate turn
            turn = 1 - turn
        
        # If turn is 0 after the loop, Maria made the last move, so Ben loses
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
