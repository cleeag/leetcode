import os
from os.path import join


def subsetsWithDup(nums):
    d = {}
    for n in nums:
        if n in d: d[n] += 1
        else: d[n] = 1

    ans = [[]]
    for idx, (k, v) in enumerate(d.items()):
        # if idx == 0:
            # ans = [[k] * i for i in range(v + 1)]
        # else:
        new_ans = [x + [k] * i for x in ans for i in range(1, v + 1) ]
        ans.extend(new_ans)
        print(new_ans)
        print(ans)
        print()



if __name__ == '__main__':
    nums = [1,2,2]
    subsetsWithDup(nums)