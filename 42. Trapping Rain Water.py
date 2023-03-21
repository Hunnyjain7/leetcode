from typing import List


class Solution(object):
    def trap(self, height: List[int]) -> int:  # noqa
        """
        :type height: List[int]
        :rtype: int
        """
        units = 0
        largest_idx = 0
        for i in range(1, len(height)):
            if height[i] >= height[largest_idx]:
                consider = height[largest_idx: i + 1]
                min_c = min(height[largest_idx], height[i])
                for j in range(1, len(consider) - 1):
                    units += min_c - consider[j]
                largest_idx = i

        while largest_idx + 1 <= len(height) - 1:
            next_largest_idx = largest_idx + 1
            for i in range(largest_idx + 1, len(height)):
                if height[i] >= height[next_largest_idx]:
                    next_largest_idx = i

            consider = height[largest_idx: next_largest_idx + 1]

            min_c = min(height[largest_idx], height[next_largest_idx])
            for j in range(1, len(consider) - 1):
                units += min_c - consider[j]
            largest_idx = next_largest_idx

        return units


if __name__ == '__main__':
    print(Solution().trap([4, 2, 0, 3, 2, 5]))
