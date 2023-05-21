from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:  # noqa
        s_len = len(s)
        if s_len < 4 or s_len > 12:
            return []

        s = [_ for _ in s]
        ips = []

        def combinations(i, ns, new):
            if i >= s_len:
                if len(new) == 4:
                    valid, op = self.validate_ip(new)
                    if valid and op not in ips:
                        ips.append(op)
                return
            new.append(ns[i:i + 3])
            combinations(i + 3, ns, new)
            new.pop()
            new.append(ns[i:i + 2])
            combinations(i + 2, ns, new)
            new.pop()
            new.append(ns[i:i + 1])
            combinations(i + 1, ns, new)
            new.pop()

        combinations(0, s, [])
        return ips

    @staticmethod
    def validate_ip(arr):
        valid = True
        op = ""
        for n in arr:
            a = ""
            for e in n:
                a += e
            if (len(a) != 1 and a[0] == "0") or int(a) not in range(0, 256):
                valid = False
                break
            op += a + "."
        return valid, op[:-1]


if __name__ == '__main__':
    print(Solution().restoreIpAddresses("010010"))
