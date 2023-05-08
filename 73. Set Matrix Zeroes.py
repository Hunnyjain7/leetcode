from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:  # noqa
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_len = len(matrix)
        col_len = len(matrix[0])
        hashmap = {}
        r = 0
        while r < row_len:
            store = []
            for c in range(0, col_len):
                if matrix[r][c] == 0:
                    a, b = r, c
                    for i in range(0, row_len):
                        store.append([i, c])
                    for i in range(0, col_len):
                        store.append([r, i])
                    hashmap[a, b] = store
            r += 1

        for key, value in hashmap.items():
            for i in value:
                matrix[i[0]][i[1]] = matrix[key[0]][key[1]]
        print(matrix)


if __name__ == '__main__':
    print(Solution().setZeroes(
        [
            [1, 2, 3, 4],
            [5, 0, 7, 8],
            [0, 10, 11, 12],
            [13, 14, 15, 0]
        ]
    ))
