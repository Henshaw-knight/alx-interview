#!/usr/bin/python3
"""minOperations function module.

Solved challenge using Prime Factorization
"""


def minOperations(n):
    """
      Calculates the minimum number of operations to achieve exactly n
      H characters using only 'Copy All' and 'Paste' operations.

      Args:
        n (int): The target number of H characters.

      Returns:
        int: The fewest number of operations needed to reach n characters.
             Returns 0 if n is impossible to achieve.
    """
    result = []
    divisor = 2
    if n <= 1:
        return 0
    while (n > 1):
        while (n % divisor == 0):
            result.append(divisor)
            n = n // divisor
        divisor += 1

    return sum(result)
