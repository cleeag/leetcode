import os
from os.path import join


def numDecodings(s):
    if len(s) == 0: return 0

    dp = [0] * len(s)
    dp[0] = 1
    s += "1"
    for i in range(1, len(s) - 1):
        dp[i] = dp[i-1]
        if s[i] != "0" \
                and (s[i - 1] == "1" or (s[i - 1] == "2" and 0 < int(s[i]) < 7)) \
                and s[i+1] != "0":
            dp[i] += 1

        print(dp)
    return dp[-1]



if __name__ == '__main__':
    s = "2206"
    s = "102"
    numDecodings(s)
