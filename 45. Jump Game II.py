from typing import List


class Solution:
    count = float("inf")

    def jump(self, nums: List[int]) -> int:
        def dfs(i, store):
            if i == len(nums) - 1:
                print(store)
                self.count = min(self.count, store)
                return
            if store > self.count and i >= len(nums):
                return
            for j in range(1, nums[i] + 1):
                if i + j < len(nums) and (store + 1) < self.count:
                    if nums[i + j] == 0:
                        continue
                    dfs(i + j, store + 1)

        dfs(0, 0)
        return self.count


if __name__ == '__main__':
    print(Solution().jump([8,2,4,4,4,9,5,2,5,8,8,0,8,6,9,1,1,6,3,5,1,2,6,6,0,4,8,6,0,3,2,8,7,6,5,1,7,0,3,4,8,3,5,9,0,4,0,1,0,5,9,2,0,7,0,2,1,0,8,2,5,1,2,3,9,7,4,7,0,0,1,8,5,6,7,5,1,9,9,3,5,0,7,5]))
    # print(max([1]))
