from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:  # noqa
        cols = set()
        pos_diag = set()  # (r + c)
        neg_diag = set()  # (r - c)
        board = [["."] * n for _ in range(n)]
        res = []

        def backtrack(r):
            if r >= n:
                res.append(["".join(i) for i in board])
                return

            for c in range(n):
                if c in cols or (r + c) in pos_diag or (r - c) in neg_diag:
                    continue

                cols.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"

                backtrack(r + 1)

                cols.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."

        backtrack(0)
        return res

    def solveNQueens2(self, n: int) -> List[List[str]]:  # noqa
        if n == 1:
            return [["Q"]]
        if n == 3:
            return []
        prevs = [["." * n] * n for _ in range(1, n - 1)]
        a = 1
        for prev in prevs:
            r, c = 0, 0
            r_end = len(prev[0])
            c_end = len(prev)
            prev[r] = prev[r][:a] + "Q" + prev[r][a + 1:]
            initial = True
            prev_pos = None
            displacement = False
            dis_count = 0
            while r < r_end and c < c_end:
                positions = [None, None, None, None, None, None, None, None]
                if (r - 1) >= 0:
                    if (c - 1) >= 0:
                        positions[0] = prev[r - 1][c - 1]
                    positions[1] = prev[r - 1][c]
                    if (c + 1) < len(prev):
                        positions[2] = prev[r - 1][c + 1]
                if (c + 1) < len(prev):
                    positions[4] = prev[r][c + 1]
                    if (r + 1) < len(prev):
                        positions[7] = prev[r + 1][c + 1]
                if (c - 1) >= 0:
                    positions[3] = prev[r][c - 1]
                if (r + 1) < len(prev):
                    positions[6] = prev[r + 1][c]
                    if (c - 1) >= 0:
                        positions[5] = prev[r + 1][c - 1]
                if "Q" not in positions and not initial:
                    prev[r] = prev[r][:c] + "Q" + prev[r][c + 1:]
                if prev[r].count("Q") > 1:
                    got = False
                    for i in range(len(prev[r])):
                        if got and prev[r][i] == "Q":
                            prev[r] = prev[r][:i] + "." + prev[r][i + 1:]
                        elif prev[r][i] == "Q":
                            got = True
                if r == 1 and c == 3 and a == 2:
                    prev_pos = prev[r]
                if prev_pos == "Q..." and prev[r] == "..Q.":
                    displacement = True
                if displacement and c == c_end - 1:
                    prev[r] = "." + prev[r][:-1]
                    dis_count += 1
                initial = False
                if c == c_end - 1:
                    c = 0
                    r += 1
                    dis_count = 0
                else:
                    c += 1
            a += 1
        return prevs


# [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
if __name__ == '__main__':
    print(Solution().solveNQueens(4))
