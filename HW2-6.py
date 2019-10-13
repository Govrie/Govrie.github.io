#!/usr/bin/env python3 -tt
"""File: hello.py """
def get_two_sum(nums, target):
    nums_dict = dict(enumerate(nums))
    for i in nums_dict.keys():
        if (target - nums_dict[i]) in nums_dict.values():
            return i, list(nums_dict.keys())[list(nums_dict.values()).index(target - nums_dict[i])]
    return None
#Run only if called as a script
if __name__ == '__main__':
    nums  = [2, 7, 11, 15]
    target = 9
    print(get_two_sum(nums, target))
