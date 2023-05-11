from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:  # noqa
        hashmap = {}
        nums_len = len(nums)
        for i in range(nums_len):
            if nums[i] not in hashmap.keys():
                hashmap[nums[i]] = 1
            else:
                hashmap[nums[i]] += 1

        for key, val in hashmap.items():
            if val > 2:
                for i in range(2, val):
                    nums.remove(key)


if __name__ == '__main__':
    print(Solution().removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
