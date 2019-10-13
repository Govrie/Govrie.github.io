#!/usr/bin/env python3 -tt
"""File: hello.py """

def get_sorted_squares(nums):
    return sorted(i**2 for i in nums)

#Run only if called as a script
if __name__ == '__main__':
    nums = [-4,-1,0,3,10]
    print(get_sorted_squares(nums))
