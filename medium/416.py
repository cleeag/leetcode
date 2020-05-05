import os
from os.path import join


def canPartition(nums):
    tot = sum(nums)
    if tot % 2 != 0: return False

    def rec(nums, idx, sum, target):

        if sum == target:
            return True
        elif idx >= len(nums) or sum > target:
            return False
        if nums[idx] > target: return False

        res = False
        for i in range(idx, len(nums)):
            res = rec(nums, i + 1, sum + nums[i], target)
            if res:
                return res
        return res

    target = tot // 2
    nums = sorted(nums, reverse=True)
    res = rec(nums, 0, 0, target)
    return res


if __name__ == '__main__':
    nums = [1, 5, 11, 5]
    nums = [1, 2, 3, 5]
    nums = [2, 2]
    canPartition(nums)
