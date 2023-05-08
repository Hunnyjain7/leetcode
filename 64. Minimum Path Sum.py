from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:  # noqa
        row_len, col_len = len(grid), len(grid[0])

        for i in range(1, row_len):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, col_len):
            grid[0][i] += grid[0][i - 1]

        for r in range(1, row_len):
            for c in range(1, col_len):
                grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])
        return grid[-1][-1]

    def minPathSum3(self, grid: List[List[int]]) -> int:  # noqa
        row_len, col_len = len(grid), len(grid[0])
        memo = {}

        def back_track(r, c):
            if r >= row_len or c >= col_len:
                return float("inf")
            if r == row_len - 1 and c == col_len - 1:
                return grid[r][c]

            if (r, c) in memo:
                return memo[(r, c)]

            memo[(r, c)] = grid[r][c] + min(back_track(r + 1, c), back_track(r, c + 1))
            return memo[(r, c)]

        return back_track(0, 0)  # noqa

    def minPathSum2(self, grid: List[List[int]]) -> int:  # noqa
        row_len, col_len = len(grid), len(grid[0])

        def back_track(r, c):
            if r >= row_len or c >= col_len:
                return float("inf")
            if r == row_len - 1 and c == col_len - 1:
                return grid[r][c]

            return grid[r][c] + min(back_track(r + 1, c), back_track(r, c + 1))

        return back_track(0, 0)  # noqa

    # My first Attempt TLE
    def minPathSum1(self, grid: List[List[int]]) -> int:  # noqa
        row_len, col_len = len(grid), len(grid[0])
        steps_len = row_len + col_len - 1
        min_path = float("inf")

        def back_track(r, c, curr):
            if len(curr) == steps_len:
                nonlocal min_path
                min_path = min(sum(curr), min_path)
                return 1

            if r < row_len and c < col_len:
                curr.append(grid[r][c])

            a, b = 0, 0
            if r < row_len:
                a = back_track(r + 1, c, curr)
            if c < col_len:
                b = back_track(r, c + 1, curr)
            if a == 1 and b == 1:
                curr.pop()
            return 1

        back_track(0, 0, [])
        return min_path  # noqa


if __name__ == '__main__':
    print(Solution().minPathSum([
        [1, 3, 1],
        [6, 5, 1],
        [4, 2, 1]
    ]))
