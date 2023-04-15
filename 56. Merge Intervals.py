from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:  # noqa
        intervals.sort(key=lambda x: x[0])
        stack = []
        for i in range(len(intervals)):
            if stack and stack[0][1] >= intervals[i][0]:
                # Overlapping condition.... Update the end point accordingly...
                stack[0][1] = max(stack[0][1], intervals[i][1])
            else:
                stack.insert(0, intervals[i])
        return stack


if __name__ == '__main__':
    # print(Solution().merge([[4, 5], [1, 4], [0, 1]]))
    print(Solution().merge([[1, 4], [4, 5]]))
    # print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
