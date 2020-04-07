import os
from os.path import join


def criticalConnections(n, connections):
    from collections import defaultdict
    table = defaultdict(list)
    ans = []
    for con in connections:
        table[con[0]].append(con[1])
        table[con[1]].append(con[0])

    for k, v in table.items():
        print(k, v)
        if len(v) == 1:
            ans.append((k, v[0]))


if __name__ == '__main__':
    input = [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]]
    n = 6
    criticalConnections(6, input)