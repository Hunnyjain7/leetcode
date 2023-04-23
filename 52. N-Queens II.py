class Solution:
    def totalNQueens(self, n: int) -> int:  # noqa
        cols = set()
        pos_diag = set()
        neg_diag = set()
        board = [["."] * n for _ in range(n)]
        res = 0

        def backtrack(r):
            if r >= n:
                nonlocal res
                res += 1
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


if __name__ == '__main__':
    print(Solution().totalNQueens(4))
