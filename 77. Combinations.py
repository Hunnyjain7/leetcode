from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:  # noqa
        combs = []

        def backtrack(i, curr, l):
            if l == 0:
                combs.append(curr.copy())
            else:
                for j in range(i, n + 1):
                    curr.append(j)
                    backtrack(j + 1, curr, l - 1)
                    curr.pop()
            return combs

        return backtrack(1, [], k)


if __name__ == '__main__':
    print(Solution().combine(4, 3))
