# backtracking dfs
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        res = []
        if len(digits) == 0:
            return res
        self.dfs(digits, 0, dic, '', res)
        return res

    def dfs(self, nums, index, dic, path, res):
        if index >= len(nums):
            res.append(path)
            return
        string1 = dic[nums[index]]
        for i in string1:
            self.dfs(nums, index + 1, dic, path + i, res)


if __name__ == '__main__':
    print(Solution().letterCombinations("749"))

# for i in range(len(store)):
#     new = ""
#     for j in range(i+1, len(store)):
#         a = 0
#         while a < len(store[j][0]):
#             print(store[i][0][a], store[j][0][a])
#
#             a += 1

# my failed attempt
# class Solution(object):
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         dic = {
#             "2": "abc",
#             "3": "def",
#             "4": "ghi",
#             "5": "jkl",
#             "6": "mno",
#             "7": "pqrs",
#             "8": "tuv",
#             "9": "wxyz"
#         }
#
#         store = []
#         for i in digits:
#             value = dic.get(i, False)
#             if value:
#                 store.append([value])
#         # strings = []
#         print(store)
#
#         store_0 = 0
#         for k in range(4):
#             store_1 = 0
#             for i in range(4):
#                 store_2 = 0
#                 for j in range(4):
#                     print(store[0][0][store_0], store[1][0][store_1], store[2][0][store_2])
#                     store_2 += 1
#                 store_1 += 1
#             store_0 += 1
#

# leetcode solution
# class Solution(object):
#     def letterCombinations(self, digits):
#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#
#         if len(digits) == 0:
#             return []
#
#         mapping = {
#             '2': 'abc',
#             '3': 'def',
#             '4': 'ghi',
#             '5': 'jkl',
#             '6': 'mno',
#             '7': 'pqrs',
#             '8': 'tuv',
#             '9': 'wxyz'
#         }
#
#         combos = [x for x in mapping[digits[0]]]
#
#         for i in range(1, len(digits)):
#             new_combos = []
#             for combo in combos:
#                 new_combos += [combo + x for x in mapping[digits[i]]]
#             combos = new_combos
#         return combos
