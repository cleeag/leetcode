import os
from os.path import join


def combinationSum(candidates, target):
    def rec(ans, idx, path, sum, nums, target):
        print(ans, path, sum)
        if sum == target:
            ans.append(path)
            return
        elif sum > target:
            return

        for i in range(idx, len(nums)):
            rec(ans, i, path + [nums[i]], sum + nums[i], nums, target)

    ans = []
    rec(ans, 0, [], 0, candidates, target)
    print(ans)

    return ans


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7

    combinationSum(candidates, target)