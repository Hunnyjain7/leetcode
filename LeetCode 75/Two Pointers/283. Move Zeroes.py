"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the
non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:

Input: nums = [0]
Output: [0]

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

Follow up: Could you minimize the total number of operations done?"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:  # noqa
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        idx, count = 0, 0
        while idx < (nums_len - count):
            if nums[idx] == 0:
                nums.pop(idx)
                nums.append(0)
                count += 1
            else:
                idx += 1
        print(nums)


if __name__ == '__main__':
    print(Solution().moveZeroes([0, 1, 0, 0, 3, 12]))
