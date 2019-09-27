#!/usr/bin/env python3 -tt
"""File: hello.py """
def is_power_of_two(n):
    while abs(n) > 2:
        n = n/2
    return n == 2
#Run only if called as a script
if __name__ == '__main__':
    n = int(input("Enter a number = "))
    print(is_power_of_two(n))
