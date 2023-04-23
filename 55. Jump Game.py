from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:  # noqa
        if 0 not in nums or len(nums) == 1:
            return True
        nums_len = len(nums)
        target = nums_len - 1
        res = False

        def dp(i, store):
            nonlocal res
            if i >= target:
                res = True
                return
            if store[i] != -1:
                return store[i]
            if nums[i] == 0:
                return
            if not res:
                for j in range(nums[i], 0, -1):
                    if res:
                        break
                    dp(i + j, store)
            store[i] = res

        dp(0, [-1 for _ in range(nums_len)])
        return res


if __name__ == '__main__':
    print(Solution().canJump(
        [8, 2, 4, 4, 4, 9, 5, 2, 5, 8, 8, 0, 8, 6, 9, 1, 1, 6, 3, 5, 1, 2, 6, 6, 0, 4, 8, 6, 0, 3, 2, 8, 7, 6, 5, 1, 7,
         0, 3, 4, 8, 3, 5, 9, 0, 4, 0, 1, 0, 5, 9, 2, 0, 7, 0, 2, 1, 0, 8, 2, 5, 1, 2, 3, 9, 7, 4, 7, 0, 0, 1, 8, 5, 6,
         7, 5, 1, 9, 9, 3, 5, 0, 7, 5]))
