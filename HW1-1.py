#!/usr/bin/env python3 -tt
"""File: hello.py """
def get_digit_sum(n):
    string_repr = str(abs(n))
    digits_sum = 0
    for digit in string_repr:
        digits_sum +=int(digit)
    return digits_sum
#Run only if called as a script
if __name__ == '__main__':
    print(get_digit_sum(1123))
