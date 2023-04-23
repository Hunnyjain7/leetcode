from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:  # noqa
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        stack = []
        for i in range(len(intervals)):
            if stack and stack[0][1] >= intervals[i][0]:
                stack[0][1] = max(stack[0][1], intervals[i][1])
            else:
                stack.insert(0, intervals[i])
        return stack[::-1]


if __name__ == '__main__':
    print(Solution().insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
