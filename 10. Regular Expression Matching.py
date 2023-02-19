class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s_index = 0
        new_str = ""
        skip = 0
        it_braked = False
        for i in range(len(p)):
            j = i + 1
            if skip > 0:
                skip -= 1
            elif not s_index < len(s):
                if not it_braked:
                    new_str += p[i]
                break
            elif (p[i] != "." and p[i] != "*") and j < len(p) and p[j] == '*':
                skip += 1
                initial_skip = True
                for k in range(s_index, len(s)):
                    if s[k] == p[i]:
                        if initial_skip:
                            initial_skip = False
                            skip -= 1
                        else:
                            skip += 1
                        new_str += s[k]
                        s_index += 1
                    else:
                        it_braked = True
                        break
            elif p[i] == '*' or p[i] == ".":
                l = j + 1
                if j < len(p) and l < len(p) and p[i] == "." and p[j] == '*' and p[l] != "*" and p[l] != ".":
                    temp = ""
                    for m in range(i, len(s)):
                        if p[l] == s[m]:
                            new_str += temp
                            s_index += len(temp)
                            break
                        temp += s[m]
                    skip += 2
                elif j < len(p) and p[i] == "." and p[j] == '*':
                    new_str += s[s_index]
                    s_index += 1
                elif j < len(p) and p[i] == "." and p[j] != '*':
                    new_str += s[s_index]
                    s_index += 1
                else:
                    new_str += s[s_index]
                    s_index += 1
                    skip += 1
            elif p[i] == s[s_index]:
                new_str += s[s_index]
                s_index += 1
        return True if s == new_str else False


if __name__ == '__main__':
    # print(Solution().isMatch("mississippi", "mis*is*p*."))
    # print(Solution().isMatch("aaa", "a*a"))
    # print(Solution().isMatch("mississippi", "mis*is*ip*."))
    # print(Solution().isMatch("aaa", "ab*a*c*a"))
    print(Solution().isMatch("aaba", "ab*a*c*a"))

    import re

    # print(re.match("mis*is*p*.", "mississippi"))

# for i, j in zip(s, p):
#     if asteris:
#         new_str += i
#     elif i == j or j == ".":
#         new_str += i
#     elif j == "*":
#         asteris = True
#         new_str += i
# return True if s == new_str else False


# asteris = False
#         new_str = ""
#         i = 0
#         p_c = 0
#         while len(s) != i and len(p) != p_c:
#             if asteris:
#                 if p[p_c] != "*":
#                     p_c += 1
#                     new_str += s[i]
#                 else:
#                     asteris = False
#                     p_c += 1
#                     continue
#             elif p_c < len(p) and (s[i] == p[p_c] or p[p_c] == "."):
#                 new_str += s[i]
#                 p_c += 1
#             elif p_c < len(p) and p[p_c] == "*":
#                 asteris = True
#                 p_c += 1
#                 new_str += s[i]
#             else:
#                 p_c += 1
#                 continue
#             i += 1
#         return True if s == new_str else False
