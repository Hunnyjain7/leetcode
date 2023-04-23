class Solution:
    def getPermutation(self, n: int, k: int) -> str:  # noqa
        nums = [i for i in range(1, n + 1)]

        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i - 1] * i

        k -= 1
        res = []
        i = n - 1
        while nums:
            index = k // factorial[i]
            res.append(str(nums[index]))
            nums.pop(index)
            k = k % factorial[i]
            i -= 1
        return ''.join(res)

    # TLE
    def getPermutation2(self, n: int, k: int) -> str:  # noqa
        numbers = [i for i in range(1, n + 1)]
        perms = [[]]
        for number in numbers:
            nexts = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    perm_copy = perm.copy()
                    perm_copy.insert(i, number)
                    nexts.append(perm_copy)
            perms = nexts
        perms.sort()
        return "".join(str(i) for i in perms[k - 1])


if __name__ == '__main__':
    print(Solution().getPermutation2(4, 3))
