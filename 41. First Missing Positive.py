from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:  # noqa
        nums.sort()
        count = 1
        prev = None
        for i in range(len(nums)):
            if nums[i] > 0:
                for j in range(i, len(nums)):
                    if nums[j] == prev:
                        continue
                    if nums[j] != count:
                        return count
                    prev = nums[j]
                    count += 1
                break
        return count


if __name__ == '__main__':
    print(Solution().firstMissingPositive([0, 2, 2, 1, 1]))
