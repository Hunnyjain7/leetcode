from typing import List


class Solution(object):
    def combinationSum(self, candidates, target):  # noqa
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        currset, subsets = [], set()
        candidates_len = len(candidates)

        def combination(i, currset, currsum):  # noqa
            curr = currset.copy()
            if currsum > target:
                return
            if currsum == target:
                subsets.add(tuple(curr))
                return
            if i >= candidates_len:
                return

            for j in range(i, candidates_len):
                combination(j, currset + [candidates[j]], currsum + candidates[j])

        combination(0, currset, 0)
        subsets = list(subsets)
        return subsets

    def combinationSum3(self, candidates: List[int], target: int) -> List[List[int]]:  # noqa
        store = set()
        for i in range(len(candidates)):
            for j in (i + 1, len(candidates) + 1):
                sub = candidates[i:j]
                if sum(sub) == target:
                    store.add(tuple(sub))

                muls = [1 for _ in sub]

                k = i
                mul_idx = 0
                while k < j and mul_idx < len(muls):
                    if sum([candidates[k] * muls[mul_idx]]) <= target:
                        if sum([candidates[k] * muls[mul_idx]]) == target:
                            store.add(tuple([candidates[k] * muls[mul_idx]]))
                        muls[mul_idx] += 1
                    else:
                        k += 1
                        mul_idx += 1
                print(muls)
        store = [list(i) for i in store]
        return store

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:  # noqa
        store = list()
        last = len(candidates) - 1
        mul = 1
        for i in range(len(candidates)):
            if candidates[i] == target:
                store.append([candidates[i]])
                here = False
            while i <= last:
                print(i, last, candidates[i], candidates[last])
                if candidates[i] + (candidates[last] * mul) <= target:
                    here = True
                    if candidates[i] + (candidates[last] * mul) == target:
                        a = [candidates[last] for _ in range(mul)]
                        a.append(candidates[i])
                        a.sort()
                        if a not in store:
                            store.append(a)
                if candidates[last] + (candidates[i] * mul) <= target:
                    here = True
                    if candidates[last] + (candidates[i] * mul) == target:
                        a = [candidates[i] for _ in range(mul)]
                        a.append(candidates[last])
                        a.sort()
                        if a not in store:
                            store.append(a)
                if (candidates[last] * mul) + (candidates[i] * mul) <= target:
                    here = True
                    if (candidates[last] * mul) + (candidates[i] * mul) == target:
                        a = [candidates[i] for _ in range(mul)] + [candidates[last] for _ in range(mul)]
                        a.sort()
                        if a not in store:
                            store.append(a)
                else:
                    here = False
                    last -= 1
                    mul = 1
                if here:
                    mul += 1
            last = len(candidates) - 1
        return store


if __name__ == '__main__':
    print(Solution().combinationSum([2, 3, 6, 7], 7))
