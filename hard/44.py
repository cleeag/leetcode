import os
from os.path import join


def isMatch(s, p):
    table = [[0 for _ in range(len(s))] for _ in range(len(p))]
    ans = False

    lower_bound = 0
    for i in range(0, len(p)):
        new_lb = len(s)
        if p[i] == '*':
            for j in range(max(0, lower_bound - 1), len(s)):
                table[i][j] = 2
            # print(p[i], table[i], lower_bound)
            continue

        alive = False
        for j in range(lower_bound, len(s)):
            if p[i] == '?' or p[i] == s[j]:
                if i > 0 and j > 0:
                    if table[i - 1][j - 1] != 0:
                        table[i][j] = 1
                elif i == 0 and j == 0:
                    table[i][j] = 1
                elif i > 0 and j == 0:
                    if table[i - 1][j] == 2:
                        table[i][j] = 1
                if table[i][j] != 0:
                    new_lb = min(j + 1, new_lb)
                    alive = True
        lower_bound = new_lb
        print(p[i], table[i], lower_bound)
        if not alive: break


    if len(s) == 0 and len(p) == 0: ans =  True
    elif len(s) != 0 and len(p) == 0: ans = False
    elif len(s) == 0:
        for c in p:
            if c != '*':
                ans = False
                break
        else:
            ans = True
    elif table[-1][-1] != 0:
        ans = True
    print(ans)
    return ans


if __name__ == '__main__':
    s = "adceb"
    p = "*a*b"
    # s = "acdcb"
    # p = "a*c?b"
    # s = "cb"
    # p = "*"
    s = "mississippi"
    p = "m??*ss*?i*pi"
    s = "a"
    p = "a*"
    # s = "b"
    # p = "?*?"
    # s = "zacabz"
    # p = "*a?b*"

    isMatch(s, p)
