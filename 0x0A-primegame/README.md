Explanation of the Code

    sieve_of_eratosthenes(n):
        This function generates a list of primes up to n using the Sieve of Eratosthenes. It marks non-prime numbers in a boolean array, and then collects the primes.

    isWinner(x, nums):
        This function simulates x rounds of the game.
        For each round, it calculates the primes up to n (from nums list).
        It alternates turns between Maria (who starts first) and Ben, removing primes and their multiples from the set.
        After all the primes are removed, the player who cannot make a move loses the round.

    Game Simulation:
        For each round, the set of primes is used to simulate the turn-based game. The smallest available prime is picked each turn, and its multiples are removed.
        The round ends when no primes are available, and the winner is determined by who made the last valid move.

    Winner Calculation:
        The total number of wins for Maria and Ben is tracked.
        The function returns the player with the most wins, or None if it’s a tie.

Example

For the input x = 3 and nums = [4, 5, 1]:

isWinner(3, [4, 5, 1])

