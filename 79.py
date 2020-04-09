import os
from os.path import join


def exist(board, word):
    def rec(board, word, i, j, word_i, been):
        print(i, j, word[:word_i], word_i)
        if word_i == len(word) - 1:
            if board[i][j] == word[word_i]:
                print('got it')
                return True
            else:
                return False
        else:
            if board[i][j] != word[word_i]:
                return False
            else:
                been[i][j] = 1
                print(been)
                a = b = c = d = False
                if i - 1 >= 0 and been[i - 1][j] == 0:
                    a = rec(board, word, i - 1, j, word_i + 1, [x[:] for x in been])
                if not a and i + 1 < len(board) and been[i + 1][j] == 0:
                    a = rec(board, word, i + 1, j, word_i + 1, [x[:] for x in been])
                if not a and j - 1 >= 0 and been[i][j - 1] == 0:
                    a = rec(board, word, i, j - 1, word_i + 1, [x[:] for x in been])
                if not a and j + 1 < len(board[0]) and been[i][j + 1] == 0:
                    a = rec(board, word, i, j + 1, word_i + 1, [x[:] for x in been])

            return a
            # return a or b or c or d

    ans = False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0]:
                been = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
                ans = rec(board, word, i, j, 0, been)
            if ans: break
        if ans: break
    print(ans)
    return ans


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    word = "ABCCED"

    board = [
        ['A', 'B'],
    ]
    word = "BA"

    board = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    word = "AAB"

    board = [["A", "B", "C", "E"],
             ["S", "F", "E", "S"],
             ["A", "D", "E", "E"]]
    word = "ABCESEEEFS"

    exist(board, word)