"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a = 0
        while nums:
            b = nums[a]
            for i in range(a, len(nums)):
                if a == i:
                    continue
                if b + nums[i] == target:
                    return [a, i]
            a += 1


obj = Solution()
s = obj.twoSum([3, 2, 4], 6)
print(s)
