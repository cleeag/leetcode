import os
from os.path import join


def removeDuplicates(nums):
    if len(nums) == 0: return 0
    if len(nums) == 1: return 1

    i = 1
    cur = nums[0]
    cur_count = 1
    while i < len(nums):
        if cur != nums[i]:
            cur = nums[i]
            cur_count = 1
            i += 1
        elif cur == nums[i] and cur_count == 2:
            # nums = nums[:i] + nums[i + 1:]
            nums.pop(i)
        elif cur == nums[i] and cur_count < 2:
            cur_count += 1
            i += 1
        print(nums, i, cur, cur_count)
    return len(nums)

if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    nums = [0,0,1,1,1,1,2,3,3]
    nums = [1,1,1,2,2,3]
    removeDuplicates(nums)