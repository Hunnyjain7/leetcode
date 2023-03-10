from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:  # noqa
        nums[:] = sorted(set(nums))
        return len(nums)


if __name__ == '__main__':
    print(Solution().removeDuplicates([1, 1, 2]))
