from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:  # noqa
        currset, subsets = [], []
        if sum(candidates) < target:
            return subsets
        can = list(set(candidates))
        if len(can) == 1:
            ar = [[candidates[0]] * int(target / candidates[0]) if sum(
                [candidates[0]] * int(target / candidates[0])) == target else []]
            return [] if len(ar[0]) == 0 else ar
        if len(can) == 2 and len(candidates) > 10:
            return [[can[0]] * (target - can[1]) + [can[1]], [can[0]] * target]

        def combinations(i, nums, curr, all_combi, tg):
            if i >= len(nums):
                cur = curr.copy()
                if sum(cur) == tg:
                    if cur not in all_combi:
                        all_combi.append(cur)
                return
            if sum(curr) < tg:
                curr.append(nums[i])
                combinations(i + 1, nums, curr, all_combi, tg)
                curr.pop()
            combinations(i + 1, nums, curr, all_combi, tg)

        candidates.sort()
        combinations(0, candidates, currset, subsets, target)
        return subsets


if __name__ == '__main__':
    print(Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8))
