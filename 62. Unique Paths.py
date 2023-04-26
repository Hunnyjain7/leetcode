class Solution:
    def uniquePaths(self, m: int, n: int) -> int:  # noqa
        paths = [[1] * n for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                paths[row][col] = paths[row - 1][col] + paths[row][col - 1]
        return paths[-1][-1]


if __name__ == '__main__':
    print(Solution().uniquePaths(3, 7))
