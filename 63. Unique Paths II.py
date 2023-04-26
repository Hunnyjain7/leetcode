from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:  # noqa
        # for row in range(len(obstacleGrid)):
        #     for col in range(0, len(obstacleGrid[0])):
        #         obstacleGrid[row][col] = 0 if obstacleGrid[row][col] == 1 else  1
        # print(obstacleGrid)
        for row in range(len(obstacleGrid)):
            for col in range(1, len(obstacleGrid[0])):
                if obstacleGrid[row][col] == 0:
                    continue
                obstacleGrid[row][col] = obstacleGrid[row - 1][col] + obstacleGrid[row][col - 1]
        return obstacleGrid[-1][-1]


if __name__ == '__main__':
    print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
