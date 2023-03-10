from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:  # noqa
        while val in nums:
            nums.remove(val)
        return len(nums)


if __name__ == '__main__':
    print(Solution().removeElement([3, 2, 2, 3], 2))
