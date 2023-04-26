from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:  # noqa
        r = 0
        r_end = len(matrix)
        c = 0
        c_end = len(matrix[0])
        target = c_end
        count = 0
        curr = 0
        res = []
        while r < r_end and c < c_end:
            for i in range(c, c_end):
                if target == count:
                    count = 0
                    curr += 1
                res.append(matrix[r][i])
                count += 1
            r += 1
            for i in range(r, r_end):
                if target == count:
                    count = 0
                    curr += 1
                res.append(matrix[i][c_end - 1])
                count += 1
            c_end -= 1

            if r < r_end:
                for i in range(c_end - 1, c - 1, -1):
                    if target == count:
                        count = 0
                        curr += 1
                    res.append(matrix[r_end - 1][i])
                    count += 1
                r_end -= 1

            if c < c_end:
                for i in range(r_end - 1, r - 1, -1):
                    if target == count:
                        count = 0
                        curr += 1
                    res.append(matrix[i][c])
                    count += 1
                c += 1
        return res

    def spiralOrderMatrix(self, matrix: List[List[int]]) -> List[List[int]]:  # noqa
        r = 0
        r_end = len(matrix)
        c = 0
        c_end = len(matrix[0])
        target = c_end
        res = [([-1] * c_end) for _ in range(r_end)]
        count = 0
        curr = 0
        while r < r_end and c < c_end:
            print("left>right")
            for i in range(c, c_end):
                if target == count:
                    count = 0
                    curr += 1
                res[curr][count] = matrix[r][i]
                count += 1
            r += 1
            print("top>bottom")
            for i in range(r, r_end):
                if target == count:
                    count = 0
                    curr += 1
                res[curr][count] = matrix[i][c_end - 1]
                count += 1
            c_end -= 1

            if r < r_end:
                print("left<right")
                for i in range(c_end - 1, c - 1, -1):
                    if target == count:
                        count = 0
                        curr += 1
                    res[curr][count] = matrix[r_end - 1][i]
                    count += 1
                r_end -= 1

            if c < c_end:
                print("bottom>top")
                for i in range(r_end - 1, r - 1, -1):
                    if target == count:
                        count = 0
                        curr += 1
                    res[curr][count] = matrix[i][c]
                    count += 1
                c += 1
        return res


if __name__ == '__main__':
    print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
