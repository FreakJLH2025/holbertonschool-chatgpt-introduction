#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function description:
        Computes the factorial of a non-negative integer using recursion.

    Parameters:
        n (int): The non-negative integer for which the factorial is to be calculated.

    Returns:
        int: The factorial value of the input number.
             If n == 0, returns 1 (by definition of factorial).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Read the first command-line argument, convert to int, and compute factorial
f = factorial(int(sys.argv[1]))
print(f)
