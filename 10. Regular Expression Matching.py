class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        asteris = False
        new_str = ""
        i = 0
        p_c = 0
        while len(s) != i and len(p) != p_c:
            if asteris:
                if p[p_c] != "*":
                    p_c += 1
                    new_str += s[i]
                else:
                    asteris = False
                    p_c += 1
                    continue
            elif p_c < len(p) and (s[i] == p[p_c] or p[p_c] == "."):
                new_str += s[i]
                p_c += 1
            elif p_c < len(p) and p[p_c] == "*":
                asteris = True
                p_c += 1
                new_str += s[i]
            else:
                p_c += 1
                continue
            i += 1
        return True if s == new_str else False


if __name__ == '__main__':
    print(Solution().isMatch("mississippi", "mis*is*p*."))
    print(Solution().isMatch("mississippi", "mis*is*ip*."))
    print(Solution().isMatch("aab", "c*a*b"))

    import re
    print(re.match("mis*is*p*.", "mississippi"))

# for i, j in zip(s, p):
#     if asteris:
#         new_str += i
#     elif i == j or j == ".":
#         new_str += i
#     elif j == "*":
#         asteris = True
#         new_str += i
# return True if s == new_str else False
