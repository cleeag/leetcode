import os
from os.path import join


def restoreIpAddresses(s):
    def rec(ans, s, i, section, path):
        if i >= len(s): return
        if section == 3 and 0 <= int(s[i:]) < 256:
            if len(s[i:]) > 1 and s[i] == "0": return
            ans.append('.'.join([path] + [s[i:]])[1:])
        if section < 3:
            for k in range(1, 4):
                if i + k < len(s) and 0 <= int(s[i:i + k]) < 256:
                    if k > 1 and s[i] == "0": break
                    print('.'.join([path] + [s[i:i + k]]))
                    rec(ans, s, i + k, section + 1, '.'.join([path] + [s[i:i + k]]))

    ans = []
    rec(ans, s, 0, 0, "")
    print(ans)
    return ans


if __name__ == '__main__':
    s = "25525511135"
    s = "112345"
    s = "010010"
    restoreIpAddresses(s)
