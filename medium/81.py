import os
from os.path import join


def search(nums, target):
    def rec(nums, i, j, target):
        print(nums[i:j + 1])
        mid = (i + j) // 2

        if mid == i:
            return True if (nums[mid] == target or nums[j] == target) else False

        if nums[i] == nums[mid] == nums[-1]:
            return rec(nums, i, mid, target) or rec(nums, mid, j, target)
        if nums[i] <= nums[mid]:
            if nums[i] <= target <= nums[mid]:
                return rec(nums, i, mid, target)
            else:
                return rec(nums, mid, j, target)
        else:
            if nums[mid] <= target <= nums[j]:
                return rec(nums, mid, j, target)
            else:
                return rec(nums, i, mid, target)

    if len(nums) == 0:
        ans = False
    else:
        ans = rec(nums, 0, len(nums) - 1, target)
    print(ans)
    return ans


if __name__ == '__main__':
    nums = [2, 3, 6, 0, 0, 1, 2]
    nums = [1]
    nums = [1,3,1,1,1]
    nums = [1, 1, 1,3,1,1,1]
    target = 2
    search(nums, target)
