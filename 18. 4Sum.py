class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        print(nums)
        s = set()
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            l = k - 1
            while j < k:
                m = l
                while j < m:
                    l_sum = nums[i] + nums[j] + nums[m] + nums[k]
                    if l_sum == target and m < k:
                        print("inner", i, j, m, k)
                        s.add((nums[i], nums[j], nums[m], nums[k]))
                    m -= 1
                if k >= l:
                    k -= 1
                    l -= 1
                sum = nums[i] + nums[j] + nums[l] + nums[k]
                if sum == target and l < k:
                    print(i, j, l, k)
                    s.add((nums[i], nums[j], nums[l], nums[k]))
                    j += 1
                    l -= 1
                elif sum < target:
                    j += 1
                elif sum > target:
                    l -= 1

        return list(s)


# [[[-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],[-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
if __name__ == '__main__':
    print(Solution().fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0))
