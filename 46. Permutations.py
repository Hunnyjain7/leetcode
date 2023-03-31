class Solution(object):
    def permute(self, nums):  # noqa
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

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
                    res_perms.append(pcopy)
                res += res_perms
            return res

        return permutations(0, nums)


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
