from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:  # noqa
        comm = []

        def subset(i, curr):
            if i >= len(nums):
                comm.append(curr.copy())
                return
            curr.append(nums[i])
            subset(i + 1, curr)
            curr.pop()
            subset(i + 1, curr)

            return comm

        return subset(0, [])


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
