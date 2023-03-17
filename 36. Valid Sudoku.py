from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:  # noqa
        for i in range(0, len(board)):
            cols = []
            for o in range(9):
                if board[o][i] != ".":
                    if board[o][i] in cols:
                        return False
                    cols.append(board[o][i])
            if i in [0, 3, 6]:
                mid_board = board[i:i + 3]
                for j in range(3):
                    mid_nums = []
                    for n in mid_board[j]:
                        if n != ".":
                            if n in mid_nums:
                                return False
                            mid_nums.append(n)
                    for k in range(0, 9, 3):
                        try:
                            a = mid_board[j][k:k + 3]
                            b = mid_board[j + 1][k:k + 3]
                            c = mid_board[j + 2][k:k + 3]
                        except:  # noqa
                            break
                        nums = []
                        for p in a + b + c:
                            if p != ".":
                                if p in nums:
                                    return False
                                nums.append(p)
        return True


if __name__ == '__main__':
    print(Solution().isValidSudoku([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]))
