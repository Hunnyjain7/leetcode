from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:  # noqa
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        paths = [[0] * (n + 1) for _ in range(m + 1)]
        paths[0][1] = 1
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if not obstacleGrid[row - 1][col - 1]:
                    paths[row][col] = paths[row - 1][col] + paths[row][col - 1]
        return paths[-1][-1]

    # passed
    def uniquePathsWithObstacles2(self, obstacleGrid: List[List[int]]) -> int:  # noqa
        def memoization(r, c, rows, cols, cache):
            """Top Down Dynamic Programming Approach."""
            if r == rows or c == cols:
                return 0
            if cache[r][c] == -2:
                return 0
            if cache[r][c] > 0:
                return cache[r][c]
            if r == rows - 1 and c == cols - 1:
                return 1
            cache[r][c] = memoization(r + 1, c, rows, cols, cache) + memoization(r, c + 1, rows, cols, cache)
            return cache[r][c]

        replacements = {0: -1, 1: -2}
        replacer = replacements.get
        obstacleGrid = [[replacer(n, n) for n in k] for k in obstacleGrid]
        return memoization(0, 0, len(obstacleGrid), len(obstacleGrid[0]), obstacleGrid)

    # Failed
    def uniquePathsWithObstacles3(self, obstacleGrid: List[List[int]]) -> int:  # noqa
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        if len(obstacleGrid) == 1 or len(obstacleGrid[0]) == 1:
            for row in obstacleGrid:
                for col in row:
                    if col == 1:
                        return 0
            return 1

        if len(obstacleGrid[0]) == 2:
            count = 0
            for row in obstacleGrid:
                for col in row:
                    if col == 1:
                        if count == 2:
                            break
                        count += 1
            return 2 - count

        for row in range(len(obstacleGrid)):
            for col in range(1, len(obstacleGrid[0])):
                obstacleGrid[row][col] = -2 if obstacleGrid[row][col] == 1 else -1
                if obstacleGrid[row][col] == -2 or obstacleGrid[row - 1][col] == -2 or obstacleGrid[row][col - 1] == -2:
                    continue
                obstacleGrid[row][col] = obstacleGrid[row - 1][col] + obstacleGrid[row][col - 1]
        return obstacleGrid[-1][-1]


if __name__ == '__main__':
    # print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    # print(Solution().uniquePathsWithObstacles([[0, 1], [0, 0]]))
    print(Solution().uniquePathsWithObstacles([[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]))
