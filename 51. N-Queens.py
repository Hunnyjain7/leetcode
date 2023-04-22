from typing import List


class Solution:
    # Unsolved better  attempt of lettcode solutions
    # https://leetcode.com/problems/n-queens/solutions/3244489/beats-99-80-python3-solution/?languageTags=python3&topicTags=backtracking
    def solveNQueens(self, n: int) -> List[List[str]]:  # noqa
        if n == 1:
            return [["Q"]]
        if n == 3:
            return []
        prevs = [["." * n] * n for _ in range(1, n - 1)]
        a = 1
        for prev in prevs:
            r, c = 0, 0
            r_end = len(prev[0])
            c_end = len(prev)
            prev[r] = prev[r][:a] + "Q" + prev[r][a + 1:]
            initial = True
            prev_pos = None
            displacement = False
            dis_count = 0
            while r < r_end and c < c_end:
                positions = [None, None, None, None, None, None, None, None]
                if (r - 1) >= 0:
                    if (c - 1) >= 0:
                        positions[0] = prev[r - 1][c - 1]
                    positions[1] = prev[r - 1][c]
                    if (c + 1) < len(prev):
                        positions[2] = prev[r - 1][c + 1]
                if (c + 1) < len(prev):
                    positions[4] = prev[r][c + 1]
                    if (r + 1) < len(prev):
                        positions[7] = prev[r + 1][c + 1]
                if (c - 1) >= 0:
                    positions[3] = prev[r][c - 1]
                if (r + 1) < len(prev):
                    positions[6] = prev[r + 1][c]
                    if (c - 1) >= 0:
                        positions[5] = prev[r + 1][c - 1]
                if "Q" not in positions and not initial:
                    prev[r] = prev[r][:c] + "Q" + prev[r][c + 1:]
                if prev[r].count("Q") > 1:
                    got = False
                    for i in range(len(prev[r])):
                        if got and prev[r][i] == "Q":
                            prev[r] = prev[r][:i] + "." + prev[r][i + 1:]
                        elif prev[r][i] == "Q":
                            got = True
                if r == 1 and c == 3 and a == 2:
                    prev_pos = prev[r]
                if prev_pos == "Q..." and prev[r] == "..Q.":
                    displacement = True
                if displacement and c == c_end - 1:
                    prev[r] = "." + prev[r][:-1]
                    dis_count += 1
                initial = False
                if c == c_end - 1:
                    c = 0
                    r += 1
                    dis_count = 0
                else:
                    c += 1
            a += 1
        return prevs


# [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
if __name__ == '__main__':
    print(Solution().solveNQueens(4))
    # def solveNQueens(self, n: int) -> List[List[str]]:  # noqa
    #     combs = []
    #     prev = ["Q" + ("." * (n-1)) for _ in range(n)]
    #     print(prev)
    #     r, c = 0, 0
    #     r_end = len(prev[0])
    #     c_end = len(prev)
    #     while r < r_end and c < c_end:
    #         positions = [None, None, None, None, None, None, None, None]
    #         tl, t, tr, ll, rr, bl, b, br = None, None, None, None, None, None, None, None
    #         if (r - 1) >= 0:
    #             if (c - 1) >= 0:
    #                 tl = prev[r - 1][c - 1]
    #             t = prev[r - 1][c]
    #             if (c + 1) < len(prev):
    #                 tr = prev[r - 1][c + 1]
    #         if (c + 1) < len(prev):
    #             rr = prev[r][c + 1]
    #             if (r + 1) < len(prev):
    #                 br = prev[r + 1][c + 1]
    #         if (c - 1) >= 0:
    #             ll = prev[r][c - 1]
    #         if (r + 1) < len(prev):
    #             b = prev[r + 1][c]
    #             if (c - 1) >= 0:
    #                 bl = prev[r + 1][c - 1]
    #
    #         print(tl, t, tr, ll, rr, bl, b, br)
    #
    #         if c == c_end - 1:
    #             c = 0
    #             r += 1
    #         else:
    #             c += 1
    #     return combs
