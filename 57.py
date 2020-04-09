import os
from os.path import join


def insert(intervals, newInterval):
    # if len(intervals) == 1:
    #     return [[min(intervals[0][0], newInterval[0]), max(intervals[0][1], newInterval[1])]]
    if len(intervals) == 0:
        return [newInterval]

    start_between_intervals = end_between_intervals = False
    start = end = 0
    for i, interval in enumerate(intervals):
        if intervals[i][0] <= newInterval[0] <= intervals[i][1]:
            start = i
        if i + 1 < len(intervals) and intervals[i][1] < newInterval[0] < intervals[i + 1][0]:
            start = i + 1
            start_between_intervals = True
        if i == 0 and newInterval[0] < intervals[i][0]:
            start = i
            start_between_intervals = True
        if i == len(intervals) - 1 and newInterval[0] > intervals[i][1]:
            start = i + 1
            start_between_intervals = True

        if intervals[i][0] <= newInterval[1] <= intervals[i][1]:
            end = i
        if i + 1 < len(intervals) and intervals[i][1] < newInterval[1] < intervals[i + 1][0]:
            end = i + 1
            end_between_intervals = True
        if i == len(intervals) - 1 and newInterval[1] > intervals[i][1]:
            end = i
            end_between_intervals = True

    if start_between_intervals and end_between_intervals:
        ans = intervals[:start] + [newInterval]+ intervals[end:]
    elif start_between_intervals:
        ans = intervals[:start] + [[newInterval[0], intervals[end][1]]] + intervals[end + 1:]
    elif end_between_intervals:
        ans = intervals[:start] + [[intervals[start][0], newInterval[1]]] + intervals[end:]
    else:
        ans = intervals[:start] + [[intervals[start][0], intervals[end][1]]] + intervals[end + 1:]

    print(start_between_intervals, end_between_intervals, start, end, ans)
    return ans



if __name__ == '__main__':
    intervals = [[1,3],[6,9]]
    newInterval = [2,5]
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    intervals = []
    newInterval = [4, 8]
    intervals = [[1, 5]]
    newInterval = [2, 3]
    ans = insert(intervals, newInterval)
    print(ans)
