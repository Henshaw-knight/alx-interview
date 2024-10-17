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
    basic_prime_nums = [2, 3, 5, 7, 11]
    result = []
    i = 0
    while (n != 1 and n > 0):
        divisor = basic_prime_nums[i]

        if (n % divisor == 0):
            result.append(divisor)
            n = n/divisor
        else:
            i += 1
    return sum(result)
