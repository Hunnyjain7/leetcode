from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:  # noqa
        if not matrix:
            return 0

        col_len = len(matrix[0])
        heights = [0] * (col_len + 1)
        area = 0

        for row in matrix:
            for i in range(col_len):
                heights[i] = heights[i] + 1 if row[i] == "1" else 0

            stack = [-1]
            for i in range(col_len + 1):
                while heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    w = i - stack[-1] - 1
                    area = max(area, h * w)
                stack.append(i)
        return area


if __name__ == '__main__':
    print(Solution().maximalRectangle(
        [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]
        ]
    ))
