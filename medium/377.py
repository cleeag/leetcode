import os
from os.path import join
from tqdm import tqdm

def combinationSum4_TLE(nums, target):
    def rec(ans, idx, path, sum, nums, target):
        # print(ans, path, sum)
        if sum == target:
            ans.append(path)
            return
        elif sum > target:
            return

        for i in range(idx, len(nums)):
            rec(ans, i, path + [nums[i]], sum + nums[i], nums, target)

    combs = []
    rec(combs, 0, [], 0, nums, target)

    def rec_perm(ans, nums, path):
        if len(nums) == 0:
            ans.append(path)
            return
        dup = set()
        # print(path)
        for i in range(len(nums)):
            if nums[i] not in dup:
                dup.add(nums[i])
                rec_perm(ans, nums[:i] + nums[i + 1:], path + [nums[i]])

    ans = []
    for x in combs:
        rec_perm(ans, x, [])
    return ans


def combinationSum4(nums, target):
    dp = [-1 for _ in range(target)]

    def rec(nums, target):
        if target == 0:
            return 1

        res = 0
        for i in range(len(nums)):
            if nums[i] <= target:
                if dp[target - nums[i]] == -1:
                    dp[target - nums[i]] = rec(nums, target - nums[i])
                    print(dp)
                res += dp[target - nums[i]]
        return res

    res = 0
    res += rec(nums, target)
    print(res)
    return res



if __name__ == '__main__':
    # nums = [1,2,3]
    # combinationSum4(nums, 4)

    nums = [4,2,1]
    combinationSum4(nums, 32)