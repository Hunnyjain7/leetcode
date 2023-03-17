from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:  # noqa
        indexes = []
        while target in nums:
            indexes.append(nums.index(target))
            nums[nums.index(target)] = "__SEPARATOR__"  # noqa
        if len(indexes) == 1:
            indexes += indexes
        if len(indexes) > 2:
            indexes = [indexes[0]] + [indexes[-1]]
        return indexes if indexes else [-1, -1]


if __name__ == '__main__':
    print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))
