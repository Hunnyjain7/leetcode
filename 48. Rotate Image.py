from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:  # noqa
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for r in range(len(matrix)):
            for c in range(r):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    # Failed Attempt
    def rotate2(self, matrix: List[List[int]]) -> None:  # noqa
        """
        Do not return anything, modify matrix in-place instead.
        """
        c = 0
        cl = len(matrix[0])
        while c < cl:
            last = cl
            for i in range(c, last):
                matrix[c][last - 1], matrix[i][c] = matrix[i][c], matrix[c][last - 1]
                print(matrix)
                print(cl - i - 1, cl - c - 1)

                last -= 1
            # cl-=1
            c += 1
        print(matrix)


if __name__ == '__main__':
    Solution().rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
