from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        cols = []
        rows = []
        boxes = []
        for i in range(0, len(board)):
            col = []
            for o in range(9):
                col.append(board[o][i])
            cols.append(col)
            if i in [0, 3, 6]:
                mid_board = board[i:i + 3]
                for j in range(3):
                    row = mid_board[j]
                    rows.append(row)
                    for k in range(0, 9, 3):
                        try:
                            a = mid_board[j][k:k + 3]
                            b = mid_board[j + 1][k:k + 3]
                            c = mid_board[j + 2][k:k + 3]
                        except:  # noqa
                            break
                        boxes.append([a, b, c])

        print("cols ::", cols)
        print("rows ::", rows)
        print("boxes ::", boxes)
        dot = True
        while True:
            for i in range(len(boxes)):
                print("boxes[i]>>", boxes[i])
                for j in range(3):
                    print("rows[i+j]>>", rows[i+j])
                quit()


if __name__ == '__main__':
    print(Solution().solveSudoku([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".7", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".5", "3", ".", ".", "1"],
        ["7", ".", ".", ".9", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]))
