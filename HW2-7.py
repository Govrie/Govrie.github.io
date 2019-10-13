#!/usr/bin/env python3 -tt
"""File: hello.py """
def get_three_sum(nums, target):
    nums_dict = dict(enumerate(nums))
    for i in range(len(nums_dict)-1):
        for j in range (i + 1, len(nums_dict)):
            if (target - nums_dict[i] - nums_dict[j]) in nums_dict.values():
                return i, j, list(nums_dict.keys())[list(nums_dict.values()).index(target - nums_dict[i]- nums_dict[j])]
    return None
#Run only if called as a script
if __name__ == '__main__':
    nums  = [2, 7, 11, 15]
    target = 24
    print(get_three_sum(nums, target))
