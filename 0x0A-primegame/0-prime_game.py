#!/usr/bin/python3

"""
Prime Game between Maria and Ben.

In each round, players take turns choosing prime numbers from a set of consecutive integers 
starting from 1 up to and including n. The chosen prime number and all its multiples are 
removed from the set. The player who cannot make a move loses the game. Maria always plays first, 
and both players play optimally.

Functions:
- sieve_of_eratosthenes(n): Returns a list of prime numbers up to n.
- isWinner(x, nums): Simulates the Prime Game and determines the winner for multiple rounds.
"""

def sieve_of_eratosthenes(n):
    """
    Returns a list of prime numbers up to n using the Sieve of Eratosthenes algorithm.
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]


def isWinner(x, nums):
    """
    Simulates the Prime Game for x rounds and determines who won the most rounds.
    Maria starts first and both players play optimally.

    Args:
        x (int): The number of rounds.
        nums (list): A list of integers representing n for each round.

    Returns:
        str or None: The player who won the most rounds ("Maria" or "Ben").
                     If the result is a tie, return None.
    """
    if not isinstance(x, int) or x <= 0:
        raise ValueError("x must be a positive integer.")
    
    if not all(isinstance(n, int) and n > 1 for n in nums):
        raise ValueError("All numbers in nums must be integers greater than 1.")
    
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n == 1:
            ben_wins += 1  # Ben wins automatically if n is 1 (no primes available)
            continue
        
        primes = sieve_of_eratosthenes(n)
        current_set = set(range(1, n + 1))  # Set of numbers from 1 to n
        turn = 0  # Maria starts first (0: Maria, 1: Ben)

        while primes:
            current_prime = primes.pop(0)  # Take the smallest prime
            # Remove the current prime and all its multiples from the current set
            current_set -= set(range(current_prime, n + 1, current_prime))
            # Filter primes to ensure they are still in the current set
            primes = [p for p in primes if p in current_set]
            # Switch turns
            turn = 1 - turn

        if turn == 0:
            maria_wins += 1  # Maria wins if it's her turn at the end
        else:
            ben_wins += 1  # Ben wins if it's his turn at the end

    # Determine who won the most rounds
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None  # If there is a tie

