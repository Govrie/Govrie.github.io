#!/usr/bin/env python3 -tt
"""File: hello.py """
def is_beauty(n):
    def get_digit_sum(n):
        string_repr = str(abs(n))
        digits_sum = 0
        for digit in string_repr:
            digits_sum +=int(digit)
        return digits_sum
    print (n % get_digit_sum(n) == 0)
#Run only if called as a script
if __name__ == '__main__':
    is_beauty(221)
