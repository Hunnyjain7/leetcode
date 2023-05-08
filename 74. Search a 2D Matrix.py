from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:  # noqa
        prev = float("-inf")
        for r in range(len(matrix)):
            curr = matrix[r]
            if prev < target and curr[-1] >= target:  # noqa
                for c in curr:
                    if c == target:
                        return True
                return False
            prev = curr[-1]
        return False


if __name__ == '__main__':
    print(Solution().searchMatrix(
        [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ],
        100
    ))
