from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:  # noqa
        stack, area = [], 0
        for height in heights + [-1]:
            count = 0
            while stack and stack[-1][1] >= height:
                w, h = stack.pop()
                count += w
                area = max(area, h * count)
            stack.append((count + 1, height))
        return area

    def largestRectangleArea1(self, heights: List[int]) -> int:  # noqa
        heights_len = len(heights)
        area = float("-inf")
        for i in range(heights_len):
            for j in range(i + 1, heights_len + 1):
                curr = heights[i:j]
                area = max(min(curr) * len(curr), area)
        return area


if __name__ == '__main__':
    print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3, 2]))
