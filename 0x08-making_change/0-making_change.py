#!/usr/bin/python3
"""makeChange function module.
   Given a pile of coins of different values, determine the
   fewest number of coins needed to meet a given amount `total`
"""


def makeChange(coins, total):
    """Function that determines the fewest number of coins needed
    to meet a given amount total
    Returns:
       fewest no. of coins to meet total
       - if total is 0 or less, 0 is returned
       - if total cannot be met by any no. of coins, -1 is returned
    Args:
       - coins: a list of the values of coins in your possession
                the value of a coin will always be an integer > 0
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0

    change = 0
    coins = sorted(coins, reverse=True)

    for coin in coins:
        while coin <= total:
            total -= coin
            change += 1
        if (total == 0):
            return change
    return -1
