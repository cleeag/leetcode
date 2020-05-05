import os
from os.path import join


def permute(nums):
    def rec(ans, nums, path):
        if len(nums) == 0:
            ans.append(path)
            return

        for i in range(len(nums)):
            rec(ans, nums[:i] + nums[i + 1:], path + [nums[i]])

    ans = []
    rec(ans, nums, [])

    return ans

if __name__ == '__main__':
    nums = [1,2,3]

    permute(nums)
