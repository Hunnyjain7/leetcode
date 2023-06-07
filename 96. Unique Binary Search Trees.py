class Solution:
    # Neetcode
    def numTrees(self, n: int) -> int:  # noqa
        cache = [1] * (n + 1)
        for nodes in range(2, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                total += (cache[root - 1] * cache[nodes - root])
            cache[nodes] = total
        return cache[-1]


if __name__ == '__main__':
    print(Solution().numTrees(19))
