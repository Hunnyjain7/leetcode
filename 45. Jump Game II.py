from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        nums_len = len(nums)
        jumps = 0
        valid_len = nums_len - 1

        def helper(i, j, step):  # noqa
            if i == 0:
                return

        for i in nums:
            for j in range(1, i):
                jumps = min(helper(i, j, 0), jumps)

        return jumps


if __name__ == '__main__':
    print(Solution().jump([2, 3, 0, 1, 4]))
    # print(max([1]))
