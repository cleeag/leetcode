import os
from os.path import join


def search(nums, target):

    def rec_search(nums, i, j, target):
        mid = (i + j) // 2
        # print(nums[i: j], mid, i, j)

        if nums[mid] == target: return mid
        elif i == j or i == j - 1: return -1

        if nums[i] <= nums[mid]:
            if nums[i] <= target <= nums[mid]:
                return rec_search(nums, i, mid, target)
            else:
                return rec_search(nums, mid, j, target)
        else:
            if nums[mid] <= target <= nums[j - 1]:
                return rec_search(nums, mid, j, target)
            else:
                return rec_search(nums, i, mid, target)

    if len(nums) == 0: return -1

    ans = rec_search(nums, 0, len(nums), target)
    print(ans)
    return ans

if __name__ == '__main__':
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 2
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 2
    nums = [3, 2]
    target = 2

    search(nums, target)