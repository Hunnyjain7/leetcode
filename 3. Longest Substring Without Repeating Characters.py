class Solution(object):
    sub_strings = []

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.subString(s)
        got = set()
        prev_large = 0
        largest_len = 0
        for a in self.sub_strings:
            got.add(a)
            if len(a) > largest_len:
                prev_large = largest_len
                largest_len = len(a)
            for i in range(len(a)):
                next_index = i + 1
                for j in range(next_index, len(a)):
                    if a[i] == a[j]:
                        if a in got:
                            got.remove(a)
                            largest_len = prev_large
                            break
        return largest_len

    def subString(self, st):
        n = len(st)
        for i in range(n):
            for j in range(i + 1, n + 1):
                self.sub_strings.append(st[i:j])
        return