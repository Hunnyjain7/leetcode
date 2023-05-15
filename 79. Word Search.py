from collections import defaultdict, Counter
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:  # noqa
        row_len = len(board)
        col_len = len(board[0])

        # Count number of letters in board and store it in a dictionary
        hashmap = defaultdict(int)
        for r in range(row_len):
            for c in range(col_len):
                hashmap[board[r][c]] += 1

        # Count number of letters in word
        # Check if board has all the letters in the word and they are atleast same count from word
        word_counter = Counter(word)
        for r in word_counter:
            if r not in hashmap or word_counter[r] > hashmap[r]:
                return False

        def dfs(i, j, k):
            # Recursion will return False if (i,j) is out of bounds or board[i][j] != word[k] which is current letter we need
            if i >= row_len or j >= col_len or i < 0 or j < 0 or k >= len(word) or word[k] != board[i][j]:
                return False

            # If this statement is true then it means we have reach the last letter in the word so we can return True
            if k == len(word) - 1:
                return True

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in directions:
                # Since we can't use the same letter twice, I'm changing current board[i][j] to -1 before traversing further
                temp = board[i][j]
                board[i][j] = "-1"
                # If dfs returns True then return True so there will be no further dfs
                if dfs(i + x, j + y, k + 1):
                    return True
                board[i][j] = temp

        # Traverse through board and if word[0] == board[i][j], call the DFS function
        for r in range(row_len):
            for c in range(col_len):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        return False

    # TLE
    def exist2(self, board: List[List[str]], word: str) -> bool:  # noqa
        row_len = len(board)
        col_len = len(board[0])
        res = False

        def backtrack(r, c, visited, curr):
            print(curr)
            if word in curr:
                nonlocal res
                res = True
            if (r, c) in visited:
                return ""
            if r >= row_len or c >= col_len or r < 0 or c < 0:
                return ""

            visited.append((r, c))
            curr += board[r][c]
            backtrack(r + 1, c, visited, curr)
            backtrack(r, c + 1, visited, curr)
            backtrack(r - 1, c, visited, curr)
            backtrack(r, c - 1, visited, curr)
            visited.pop()

        for i in range(row_len):
            for j in range(col_len):
                if res:
                    return res
                backtrack(i, j, [], "")
        return res


if __name__ == '__main__':
    print(Solution().exist(
        [
            ["a", "a", "b", "a", "a", "b"],
            ["b", "a", "b", "a", "b", "b"],
            ["b", "a", "b", "b", "b", "b"],
            ["a", "a", "b", "a", "b", "a"],
            ["b", "b", "a", "a", "a", "b"],
            ["b", "b", "b", "a", "b", "a"]
        ],
        "aaaababab")
    )
