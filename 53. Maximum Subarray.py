from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:  # noqa
        maxSum = nums[0]
        curSum = 0

        for n in nums:
            curSum = max(curSum, 0)
            curSum += n
            maxSum = max(maxSum, curSum)
        return maxSum
