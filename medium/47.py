import os
from os.path import join


def permuteUnique(nums):
    def rec(ans, nums, path):
        if len(nums) == 0:
            ans.append(path)
            return
        dup = set()
        print(path)
        for i in range(len(nums)):
            if nums[i] not in dup:
                dup.add(nums[i])
                rec(ans, nums[:i] + nums[i + 1:], path + [nums[i]])

    ans = []
    rec(ans, nums, [])
    print(ans)
    return ans



if __name__ == '__main__':
    nums = [1,1,1,2,2]
    permuteUnique(nums)