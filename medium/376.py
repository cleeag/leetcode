import os
from os.path import join


def wiggleMaxLength(nums):
    if len(nums) < 2: return len(nums)

    diff = [0] * (len(nums) - 1)
    dp = [0] * (len(nums) - 1)

    for i in range(1, len(nums)):
        diff[i - 1] = nums[i] - nums[i - 1]

    if diff[0] > 0:
        cur = 1
        dp[0] = 2
    elif diff[0] < 0:
        cur = -1
        dp[0] = 2
    else:
        cur = 0
        dp[0] = 1

    print(nums)
    print(diff)
    print(dp)
    print()
    for i in range(1, len(nums) - 1):
        if diff[i] > 0:
            if cur <= 0:
                dp[i] = dp[i-1] + 1
                cur = 1
            else:
                dp[i] = dp[i-1]
        elif diff[i] < 0:
            if cur >= 0:
                dp[i] = dp[i-1] + 1
                cur = -1
            else:
                dp[i] = dp[i-1]
        else:
            dp[i] = dp[i - 1]

        print(dp)
    return dp[-1]

if __name__ == '__main__':
    nums = [1,7,4,9,2,5]
    nums = [1,17,5,10,13,15,10,5,16,8]
    nums =  [1, 1,2,3,4,5,6,7,8,9]
    # nums = [5,5,5,5,5]
    nums = [1,1,2,3,1]
    nums = [0,0]
    wiggleMaxLength(nums)
