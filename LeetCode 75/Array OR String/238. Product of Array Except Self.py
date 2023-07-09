"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements
of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space
or space complexity analysis.)
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:  # noqa
        nums_len = len(nums)
        res = [1] * nums_len
        pre, post = 1, 1
        for i in range(nums_len):
            last = nums_len - i - 1
            res[i] *= pre
            pre *= nums[i]
            res[last] *= post
            post *= nums[last]
        return res


if __name__ == '__main__':
    print(Solution().productExceptSelf([1, 2, 3, 4]))
