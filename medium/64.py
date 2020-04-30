import os
from os.path import join

from src.helper_func import print_matrix


def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    arr = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == j == 0: arr[i][j] = grid[i][j]
            elif i == 0:
                arr[i][j] = arr[i][j - 1] + grid[i][j]
            elif j == 0:
                arr[i][j] = arr[i - 1][j] + grid[i][j]
            else:
                arr[i][j] = grid[i][j] + min(arr[i - 1][j], arr[i][j - 1])
            print_matrix(arr)
            print()


if __name__ == '__main__':
    grid = [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
    grid = [[1]]
    minPathSum(grid)
