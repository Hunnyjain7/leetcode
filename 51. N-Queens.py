from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:  # noqa
        combs = []
        prev = ["...." for _ in range(n)]
        prev = ["012", "345", "678"]
        for r in range(len(prev)):
            for c in range(r):
                tl = prev[r - 1][c - 1]
                t = prev[r - 1][c]
                ri = prev[r][c + 1]
                le = prev[c - 1][r]
                bl = prev[c + 1][r - 1]
                b = prev[c + 1][r]
                br = prev[c + 1][r + 1]

        return combs


if __name__ == '__main__':
    print(Solution().solveNQueens(4))
