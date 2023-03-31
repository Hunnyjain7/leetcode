from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:  # noqa
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
                    pcopy = "".join(pcopy)
                    res_perms.append([pcopy])
                res += res_perms
            return res

        all_perms = []
        mapper = {}
        f_res = {}
        for i in strs:
            mapped = False
            if i not in all_perms:
                lets_break = False
                for key, values in mapper.items():
                    if lets_break:
                        break
                    for value in values:
                        if [i] == value:
                            try:
                                f_res[key] += value
                            except:
                                f_res[key] = [value]
                            finally:
                                mapped = True
                                lets_break = True
                                break
            if not mapped:
                st_perm = permutations(0, i)
                f_res[i] = [i]
                mapper[i] = st_perm
                all_perms += st_perm
            print(f_res)
            # quit()
        return [[]]


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
