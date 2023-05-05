class Solution:
    def climbStairs(self, n: int) -> int:  # noqa
        memo = {1: 1, 2: 2}

        def brute_force(n):  # noqa
            if n in memo:
                return memo[n]
            else:
                memo[n] = brute_force(n - 1) + brute_force(n - 2)
                return memo[n]

        return brute_force(n)

    # My approach TLE
    def climbStairs2(self, n: int) -> int:  # noqa
        def permute_unique(nums):
            perms = [[]]
            for nu in nums:
                new_perm = []
                for perm in perms:
                    for j in range(len(perm) + 1):
                        new_perm.append(perm[:j] + [nu] + perm[j:])
                        if j < len(perm) and perm[j] == nu: break
                perms = new_perm
            return perms

        arr = [1] * n
        combos = [arr]
        all_combos = [arr]
        i = 0
        while i < n:
            temp = []
            for a in range(len(arr)):
                temp_sum = sum(temp)
                if temp_sum >= n:
                    break
                if i == a:
                    if temp_sum + 2 <= n:
                        temp.append(2)
                else:
                    if temp_sum + arr[a] <= n:
                        temp.append(arr[a])
            i += 1
            arr = temp
            if temp not in combos and sum(temp) == n:
                combos.append(temp)
                all_combos += permute_unique(temp)
        return len(all_combos)


if __name__ == '__main__':
    print(Solution().climbStairs(4))
