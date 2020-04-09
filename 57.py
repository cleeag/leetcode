import os
from os.path import join


def insert(intervals, newInterval):
    res = []
    new = newInterval
    for i, interval in enumerate(intervals):
        if interval[1] < new[0]:
            res.append(interval)
        elif interval[0] > new[1]:
            res.append(new)
            return res + intervals[i:]
        else:
            new = [min(interval[0], new[0]), max(interval[1], new[1])]
    res.append(new)

    return res


if __name__ == '__main__':
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    intervals = []
    newInterval = [4, 8]
    intervals = [[1, 5]]
    newInterval = [2, 3]
    ans = insert(intervals, newInterval)
    print(ans)
