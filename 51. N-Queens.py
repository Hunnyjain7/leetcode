from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:  # noqa
        combs = []
        prev = ["...." for _ in range(n)]
        prev = [
            "012",
            "345",
            "678"
        ]
        r, c = 0, 0
        r_end = len(prev[0])
        c_end = len(prev)
        while r < r_end and c < c_end:
            tl, t, tr, ll, rr, bl, b, br = None, None, None, None, None, None, None, None
            if (r - 1) >= 0:
                if (c - 1) >= 0:
                    tl = prev[r - 1][c - 1]
                t = prev[r - 1][c]
                if (c + 1) < len(prev):
                    tr = prev[r - 1][c + 1]
            if (c + 1) < len(prev):
                rr = prev[r][c + 1]
                if (r + 1) < len(prev):
                    br = prev[r + 1][c + 1]
            if (c - 1) >= 0:
                ll = prev[r][c - 1]
            if (r + 1) < len(prev):
                b = prev[r + 1][c]
                if (c - 1) >= 0:
                    bl = prev[r + 1][c - 1]

            print(tl, t, tr, ll, rr, bl, b, br)

            if c == c_end - 1:
                c = 0
                r += 1
            else:
                c += 1
        return combs


if __name__ == '__main__':
    print(Solution().solveNQueens(4))
