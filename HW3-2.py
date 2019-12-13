#!/usr/bin/env python3 -tt
"""File: hello.py """
import math
def devider_generator(number):
    for i in range(int(number/2)+1):
        if i> 0 and number % i == 0:
            yield i

deviders = devider_generator(1024)
for i in deviders:
    print(i)
