import os
from os.path import join

def print_matrix(mat):
    for row in mat:
        print(row)

def minDistance(word1, word2):

    def get_max_seq(tracking_board, m, n, res2, res1):
        if m == 0 or n == 0: return res2, res1
        if tracking_board[m][n] == 'match':
            res2 = [m -1] + res2
            res1 = [n-1] + res1

            return get_max_seq(tracking_board, m-1, n-1, res2, res1)
        elif tracking_board[m][n] == 'left':
            return get_max_seq(tracking_board, m, n-1, res2, res1)
        else:
            return get_max_seq(tracking_board, m-1, n, res2, res1)

    board = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
    tracking_board = [['' for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]
    for i in range(1, len(word2) + 1):
        for j in range(1, len(word1) + 1):
            if word2[i - 1] == word1[j - 1]:
                board[i][j] = board[i - 1][j - 1] + 1
                tracking_board[i][j] = 'match'

            elif board[i][j - 1] >= board[i - 1][j]:
                board[i][j] = board[i][j - 1]
                tracking_board[i][j] = 'left'

            else:
                board[i][j] = board[i - 1][j]
                tracking_board[i][j] = 'up'

    print_matrix(board)
    print_matrix(tracking_board)
    res2 = res1 = []
    res1, res2 = get_max_seq(tracking_board, len(word2), len(word1), res2, res1)

    print(res1, res2)

if __name__ == '__main__':
    a = 'intention'
    b = 'sexecutions'

    minDistance(a, b)
