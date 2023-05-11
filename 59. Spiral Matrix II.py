from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:  # noqa
        matrix = []
        a = 1
        for i in range(n):
            curr = []
            for j in range(n):
                curr.append(a)
                a += 1
            matrix.append(curr)
        r = 0
        r_end = len(matrix)
        c = 0
        c_end = len(matrix[0])
        a = 1
        while r < r_end and c < c_end:
            for i in range(c, c_end):
                matrix[r][i] = a
                print(r, i)
                a += 1
            r += 1
            for i in range(r, r_end):
                matrix[i][c_end - 1] = a
                a += 1
                print(i, c_end - 1)
            c_end -= 1
            if r < r_end:
                for i in range(c_end - 1, c - 1, -1):
                    matrix[r_end - 1][i] = a
                    a += 1
                r_end -= 1

            if c < c_end:
                for i in range(r_end - 1, r - 1, -1):
                    matrix[i][c] = a
                    a += 1
                c += 1
        return matrix


if __name__ == '__main__':
    print(Solution().generateMatrix(20))
