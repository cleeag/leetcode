import os
from os.path import join


def canJump1(nums):
    def rec(nums, cur):
        if cur == 0: return True
        can = False
        for i in range(cur - 1, -1, -1):
            if i + nums[i] >= cur:
                print(nums[i], i, nums[cur], cur)
                can = rec(nums, i)
                if can: break

        return can

    ans = rec(nums, len(nums) - 1)
    print(ans)
    return ans

def canJump(nums):
    for i in range(len(nums)):
        pass







if __name__ == '__main__':
    nums = [3,2,1,0,4]
    nums  =[2,3,1,1,4]
    nums = [2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6]
    # nums = [0, 0, 0, 3, 8]
    canJump(nums)