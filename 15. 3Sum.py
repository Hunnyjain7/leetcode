class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []

        arrays = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] < nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]

        print(nums)

        mid = len(nums) // 2
        left = mid - 1
        right = mid + 1
        arrays_index = 0
        while right < len(nums) and left >= 0:
            if nums[left] + nums[mid] + nums[right] == 0:
                new_array = [nums[left], nums[mid], nums[right]]
                if new_array not in arrays:
                    arrays.append(new_array)
                arrays_index += 1
                if left > 0:
                    left -= 1
                mid -= 1
                if right < len(nums):
                    right += 1
            elif nums[left] + nums[mid] + nums[right] > 0:
                left -= 1
            elif nums[left] + nums[mid] + nums[right] < 0:
                right += 1

        return arrays


if __name__ == '__main__':
    print(Solution().threeSum([3, 0, -2, -1, 1, 2]))
