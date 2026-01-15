#!/usr/bin/python3
import sys

def factorial(n):
    """Compute factorial of n (non-negative integer)."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    while n > 1:
        result *= n
        n -= 1   # decrement n to avoid infinite loop
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: {} <non-negative integer>".format(sys.argv[0]))
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        f = factorial(num)
        print(f)
    except ValueError as e:
        print("Error:", e)
        sys.exit(1)
