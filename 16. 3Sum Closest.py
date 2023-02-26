class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        difference = float('inf')
        value = 0

        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                add = nums[i] + nums[j] + nums[k]
                if add == target:
                    return target
                temp = abs(target - add)
                if temp < difference:
                    difference = temp
                    value = add
                if add < target:
                    j += 1
                else:
                    k -= 1
        return value


if __name__ == '__main__':
    print(Solution().threeSumClosest(
        [2, 3, 8, 9, 10], 16))
# print(i, j, k)
# print(i, j, k, ">>>>>>>>>>>>>>", target + add, "difference", difference, "add", add)
# print("difference ::", difference)
# print(nums)
# print(difference)
