#!/usr/bin/python3
"""In a text file, there is a single character H. Your text editor
 can execute only two operations in this file: Copy All and Paste.
  Given a number n, write a method that calculates the fewest number
   of operations needed to result in exactly n H characters in the file."""


def minOperations(n):
    """
    input n: int
    Returns an integer
    """
    if not isinstance(n, int):
        return 0

    res = 0

    for i in range(2, n):
        while n % i == 0:
            res += i
            n = n / i

    return res
