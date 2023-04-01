from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        nums_len = len(nums)
        jumps = 0

        def helper(i):
            if nums[i] == 0:
                return

        for i in nums:
            for j in range(1, i):
                helper(j)

        return 0


if __name__ == '__main__':
    print(Solution().jump([2, 3, 0, 1, 4]))
    # print(max([1]))
