#!/usr/bin/env python3 -tt
"""File: hello.py """

def number_of_matches(J, S):
    k = 0
    for i in J:
        for j in S:
            if i == j:
                k += 1
    return k
#Run only if called as a script
if __name__ == '__main__':
    J = 'aA'
    S = 'aAABBB'
    print(number_of_matches(J,S))
