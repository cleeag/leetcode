import os
from os.path import join


def numberOfArithmeticSlices(A):
    if len(A) == 0: return 0

    diff = [None] * (len(A))
    for i in range(1, len(A)):
        diff[i - 1] = A[i] - A[i - 1]
    diff[-1] = None
    print(diff)

    ans = 0
    start = 0
    cur = diff[0]
    for i in range(1, len(A)):
        if cur != diff[i]:
            l = i - start + 1
            ans += int((1 + l - 2) * (l - 2) / 2)
            print(i, l, int((1 + l - 2) * (l - 2) / 2))

            cur = diff[i]
            start = i
        print(i, ans)
    print(ans)
    return ans


if __name__ == '__main__':
    A = [1, 2, 3, 4, 6, 7, 8, 9, 9]
    A = [2,-1, -4, 4]
    A = []
    numberOfArithmeticSlices(A)
