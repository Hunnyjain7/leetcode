from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:  # noqa
        nums.sort()
        nums_len = len(nums)
        sets = [[]]
        for i in range(nums_len):
            curr = sets
            for c in range(len(curr)):
                c_copy = curr[c].copy()
                c_copy.insert(c, nums[i])
                if c_copy not in curr:
                    curr.append(c_copy)
            sets = curr
        return sets

    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:  # noqa
        nums.sort()
        nums_len = len(nums)
        sets = set()

        def subsets(i, curr):
            if i >= nums_len:
                sets.add(tuple(curr.copy()))
                return

            curr.append(nums[i])
            subsets(i + 1, curr)
            curr.pop()
            subsets(i + 1, curr)
            return list(sets)

        return subsets(0, [])


if __name__ == '__main__':
    print(Solution().subsetsWithDup([1, 2, 2]))
