from typing import List


class Solution:
    # Dutch National Flag algorithm
    def sortColors(self, nums: List[int]) -> None:  # noqa
        """
        Do not return anything, modify nums in-place instead.
        """
        low, mid, high = 0, 0, len(nums) - 1
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
        print(nums)

    def sortColors2(self, nums: List[int]) -> None:  # noqa
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_len = len(nums)
        for i in range(nums_len):
            for j in range(i + 1, nums_len):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        print(nums)


if __name__ == '__main__':
    Solution().sortColors([2, 0, 2, 1, 1, 0])
