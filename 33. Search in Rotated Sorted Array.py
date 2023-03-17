from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:  # noqa
        return nums.index(target) if target in nums else -1


if __name__ == '__main__':
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
