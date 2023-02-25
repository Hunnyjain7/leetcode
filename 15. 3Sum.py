class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target = 0
        nums.sort()
        s = set()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum == target:
                    s.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif sum < target:
                    j += 1
                else:
                    k -= 1
        return list(s)


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4]))

# My failed attempt
# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         if len(nums) == 3:
#             if sum(nums) == 0:
#                 return [nums]
#             else:
#                 return []
#
#         arrays = []
#
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] < nums[i]:
#                     nums[i], nums[j] = nums[j], nums[i]
#
#         mid = len(nums) // 2
#         left = mid - 1
#         right = mid + 1
#
#         arrays_index = 0
#
#         reshuffle_left = 0
#         reshuffle_mid = 0
#         reshuffle_right = 0
#         reshuffle_all = 0
#
#         while right < len(nums) and left >= 0:
#             if nums[left] + nums[mid] + nums[right] == 0:
#                 new_array = [nums[left], nums[mid], nums[right]]
#
#                 if new_array not in arrays and left != right and left != mid and mid != right:
#                     arrays.append(new_array)
#                 arrays_index += 1
#                 left -= 1
#                 mid -= 1
#                 right += 1
#             elif nums[left] + nums[mid] + nums[right] > 0:
#                 left -= 1
#             elif nums[left] + nums[mid] + nums[right] < 0:
#                 right += 1
#
#             if left == -1 and reshuffle_left == 0:
#                 mid = (len(nums) // 2) - 1
#                 left = mid - 1
#                 right = mid + 1
#                 reshuffle_left += 1
#             elif (mid == 0 or mid == (len(nums) - 1)) and reshuffle_mid == 0:
#                 mid = (len(nums) // 2) - 1
#                 left = mid - 2
#                 right = mid + 2
#                 reshuffle_mid += 1
#             elif right == len(nums) and reshuffle_right == 0:
#                 mid = (len(nums) // 2) + 1
#                 left = mid - 1
#                 right = mid + 1
#                 reshuffle_right += 1
#             elif (reshuffle_left == 1 or reshuffle_mid == 1 or reshuffle_right == 1) and reshuffle_all <= 4:
#                 if reshuffle_all == 0:
#                     mid = len(nums) // 2
#                     left = mid - 1
#                     right = mid + 2
#                 #     left, mid, right = mid, right, left
#                 if reshuffle_all == 1:
#                     mid = len(nums) // 2
#                     left = mid - 2
#                     right = mid + 1
#                 #     left, mid, right = right, left, mid
#                 if reshuffle_all == 2:
#                     mid = len(nums) // 2 - 1
#                     left = mid - 1
#                     right = mid + 1
#                 if reshuffle_all == 2:
#                     mid = len(nums) // 2
#                     left = mid - 2
#                     right = mid + 2
#
#                 #     left, mid, right = left, mid, right
#
#                 reshuffle_mid = 0
#                 reshuffle_left = 0
#                 reshuffle_right = 0
#                 reshuffle_all += 1
#
#         return arrays
#
