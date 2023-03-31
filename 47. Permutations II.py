from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:  # noqa
        def permutations(i, nums):  # noqa
            if i == len(nums):
                return [[]]

            res = []
            perms = permutations(i + 1, nums)
            for p in perms:
                res_perms = []
                for j in range(len(p) + 1):
                    pcopy = p.copy()
                    pcopy.insert(j, nums[i])
                    if pcopy not in res_perms and pcopy not in res:
                        res_perms.append(pcopy)
                res += res_perms
            return res

        return permutations(0, nums)


if __name__ == '__main__':
    print(Solution().permuteUnique([1, 2, 3]))
