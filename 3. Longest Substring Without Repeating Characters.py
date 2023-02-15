class Solution(object):

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if " " in s:
            s = s.split(" ")[0] + " "
        substring = set()
        largest = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                repeateds = set()
                newStr = s[i:j]
                substring.add(newStr)
                isRepeated = False
                for k in newStr:
                    if k in repeateds:
                        isRepeated = True
                        if newStr in substring:
                            substring.remove(newStr)
                            break
                    repeateds.add(k)
                if not isRepeated and len(newStr) > largest:
                    largest = len(newStr)
        return largest
