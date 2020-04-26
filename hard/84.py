import os
from os.path import join
from tqdm import tqdm

def largestRectangleArea_TLE(heights):
    def max_interval_len(num, left_idx):
        # print(left_idx)
        new_left_idx = []
        max_len = count = 0
        l = len(left_idx)
        for i, idx in enumerate(left_idx):
            if heights[idx] >= num:
                new_left_idx.append(idx)
                if i == 0 or (i > 0 and idx - left_idx[i - 1] == 1):
                    count += 1
                    if count > max_len: max_len = count
                else:
                    if count > max_len: max_len = count
                    count = 0
            elif heights[idx] < num :
                if count > max_len: max_len = count
                count = 0


        return max_len, new_left_idx

    max_area = 0
    if len(heights) == 0: return 0
    sorted_heights = sorted(heights)
    # print(sorted_heights)
    left_interval = [i for i in range(len(sorted_heights))]
    for h in tqdm(sorted_heights):
        max_len, left_interval = max_interval_len(h, left_interval)
        tmp_area = max_len * h
        if tmp_area > max_area: max_area = tmp_area
        # if tmp_area > h * len(sorted_heights): break
        # print(h, max_len, tmp_area, max_area, left_interval)
    print(max_area)
    return max_area

def largestRectangleArea_another_tle(heights):
        def rec(heights, i, h, w):
            # print(i, h, w, h*w)
            if i == len(heights) - 1:
                # print(max(h * w, heights[i] * (w + 1)))
                if heights[i] > h:
                    return max(h * (w + 1), heights[i])
                else:
                    return max(h * w, heights[i] * (w + 1))
            elif heights[i] <= h:
                return max(h * w, rec(heights, i + 1, heights[i], w + 1))
            elif heights[i] > h:
                return max(rec(heights, i + 1, h, w + 1), rec(heights, i + 1, heights[i], 1))

        if len(heights) == 0: return 0
        elif len(heights) == 1: return heights[0]
        ans = rec(heights, 1, heights[0], 1)
        print(ans)
        return ans

def largestRectangleArea(heights):

    stack = [-1]
    heights.append(0)
    max_area = 0
    for i, h in enumerate(heights):
        print(stack)
        while len(stack) > 0 and h < heights[stack[-1]]:
            print(max_area, heights[stack[-1]] * (i - stack[-2] - 1), stack, i)
            max_area = max(max_area, heights[stack[-1]] * (i - stack[-2] - 1))
            stack.pop()
        if h == heights[stack[-1]]:
            stack.pop()
            stack.append(i)
        if h > heights[stack[-1]]:
            stack.append(i)
    print(max_area)
    return max_area


if __name__ == '__main__':
    heights = [2, 1, 5, 6, 2, 3]
    # print(len(heights))
    heights = [2,1,2]
    heights = [0,9]
    heights = [1, 1, 4]

    largestRectangleArea(heights)