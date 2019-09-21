#!/usr/bin/env python3 -tt
"""File: hello.py """
def is_prime(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

upper_limit = int(input("Enter a number = "))
print(is_prime(upper_limit))

