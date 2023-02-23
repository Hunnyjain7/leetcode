class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1 or strs[0] == "":
            return strs[0]
        new = ""
        j = 0
        match = True
        while match:
            temp = ""
            for i in strs:
                if j < len(i) and temp == "":
                    temp = i[j]
                elif j >= len(i) or i[j] != temp:
                    temp = ""
                    match = False
                    break
            new += temp
            j += 1
        return new


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower", "flower", "flower", "flower"]))
    print(max(["flower", "flor", "flwr", "fl"]))
