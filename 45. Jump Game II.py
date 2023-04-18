from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:  # noqa
        nums_len = len(nums)
        target = nums_len - 1

        def helper(i, dp):
            if i >= target:
                return 0
            if dp[i] != -1:
                return dp[i]

            mini = float('inf')
            for j in range(1, nums[i] + 1):
                jm = 1 + helper(i + j, dp)
                mini = min(mini, jm)
            dp[i] = mini
            return dp[i]

        return helper(0, [-1 for _ in range(nums_len)])

    def jump2(self, nums: List[int]) -> int:  # noqa
        memo = [float("inf") for _ in range(len(nums))]
        memo[0] = 0
        n = len(nums) - 1
        for i in range(len(nums)):
            for j in range(i + 1, i + nums[i] + 1):
                if j >= len(memo):
                    break
                elif memo[j] > memo[i] + 1:
                    memo[j] = memo[i] + 1
        return memo[n]  # noqa


if __name__ == '__main__':
    # print(Solution().jump(
    #     [8, 2, 4, 4, 4, 9, 5, 2, 5, 8, 8, 0, 8, 6, 9, 1, 1, 6, 3, 5, 1, 2, 6, 6, 0, 4, 8, 6, 0, 3, 2, 8, 7, 6, 5, 1, 7,
    #      0, 3, 4, 8, 3, 5, 9, 0, 4, 0, 1, 0, 5, 9, 2, 0, 7, 0, 2, 1, 0, 8, 2, 5, 1, 2, 3, 9, 7, 4, 7, 0, 0, 1, 8, 5, 6,
    #      7, 5, 1, 9, 9, 3, 5, 0, 7, 5]))
    # print(Solution().jump([1, 1, 1, 1]))
    print(Solution().jump([2, 3, 1, 1, 4]))
