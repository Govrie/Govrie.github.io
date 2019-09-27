#!/usr/bin/env python3 -tt
"""File: hello.py """
def digits_sum(n):
    string_repr = str(abs(n))
    digits_sum = 0
    for digit in string_repr:
        digits_sum += int(digit)
    return digits_sum
def is_beauty(n):
    return n % digits_sum(n) == 0
#Run only if called as a script
if __name__ == '__main__':
    n = int(input("Enter a number = "))
    print(is_beauty(n))
