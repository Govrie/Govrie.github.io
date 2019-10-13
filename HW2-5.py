#!/usr/bin/env python3 -tt
"""File: hello.py """
def is_valid(braces_string):
    if len(braces_string) % 2 != 0:
        print(len(braces_string))
        return False
    else:
        n = 0
        for brace in braces_string:
            if brace == '(':
                n +=1
            if brace == ')':
                n -= 1
            if n < 0:
                return False
        return n == 0
#Run only if called as a script
if __name__ == '__main__':
    braces_string = "(((()()))"
    print(is_valid(braces_string))

