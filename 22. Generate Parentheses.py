from typing import List


class Solution:
    # My Solution
    def generateParenthesis(self, n: int) -> List[str]:
        pair_len = n * 2
        store = []

        def rec(s):
            if len(s) > pair_len:
                return
            if len(s) == pair_len:
                a = s
                while "()" in a:
                    a = a.replace("()", "")
                if len(a) == 0:
                    store.append(s)
            rec(s + "("), rec(s + ")")

        rec("(")
        return store

    # Better solution from leetcode
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return

            if left < n:
                dfs(left + 1, right, s + '(')

            if right < left:
                dfs(left, right + 1, s + ')')

        res = []
        dfs(0, 0, '')
        return res


if __name__ == '__main__':
    print(Solution().generateParenthesis(4))
