#!/usr/bin/env python3 -tt
"""File: hello.py """
def get_digit_d(n):
    string_repr = str(abs(n))
    digit_d = 0
    for digit in string_repr:
        if (n % int(digit)) > 0:
            digit_d +=1
    if digit_d == 0:
        return True
    else:
        return False
#Run only if called as a script
if __name__ == '__main__':
    n = int(input("Enter a number = "))
    print(get_digit_d(n))


