# TLE
class Solution(object):
    def fourSum(self, nums, target):  # noqa
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) < 4:
            return []
        if len(nums) == 4 and sum(list(nums)) != target:
            return []
        nums.sort()
        s = set()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                n = j + 1
                for l in range(n, k + 1):
                    for m in range(l + 1, k + 1):
                        if (nums[i] + nums[j] + nums[l] + nums[m]) == target:
                            s.add((nums[i], nums[j], nums[l], nums[m]))
                            break
                add = nums[i] + nums[j] + nums[n] + nums[k]
                if add == target:
                    if n < k:
                        s.add((nums[i], nums[j], nums[n], nums[k]))
                    k -= 1
                    j += 1
                elif add < target:
                    j += 1
                else:
                    k -= 1
        return list(s)


if __name__ == '__main__':
    print(Solution().fourSum(
        [1000000000, 1000000000, 1000000000, 1000000000], -294967296))
