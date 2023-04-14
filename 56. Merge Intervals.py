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


# [[0,5]]
# [[1,6],[8,10],[15,18]]
if __name__ == '__main__':
    print(Solution().merge([[4, 5], [1, 4], [0, 1]]))
    # print(Solution().merge([[1,4],[4,5]]))
    # print(Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]))

# if len(intervals) > 1:
#     FAFV, FASV, SAFV, SASV = (
#         intervals[-2][-2],
#         intervals[-2][-1],
#         intervals[-1][-2],
#         intervals[-1][-1],
#     )
#     if FAFV > SAFV:
#         FAFV, SAFV = SAFV, FAFV
#     if FASV > SASV:
#         FASV, SASV = SASV, FASV
#     interval_range = range(FAFV, SASV + 1)
#     FA_interval_range = range(FAFV, FASV + 1)
#     SA_interval_range = range(SAFV, SASV + 1)
#
#     if (
#             FASV in SA_interval_range and SAFV in FA_interval_range
#             and FASV in interval_range and SAFV in interval_range
#     ):
#         intervals[-2:] = [[FAFV, SASV]]


# def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#     intervals_copy = intervals.copy()
#     for i in range(len(intervals)):
#         for j in range(i + 1, len(intervals)):
#             FAFV, FASV, SAFV, SASV = (
#                 intervals[i][0],
#                 intervals[i][1],
#                 intervals[j][0],
#                 intervals[j][1],
#             )
#
#             if FAFV > SAFV:
#                 FAFV, SAFV = SAFV, FAFV
#             if FASV > SASV:
#                 FASV, SASV = SASV, FASV
#
#             interval_range = range(FAFV, SASV + 1)
#             # FA_interval_range = range(FAFV, FASV + 1)
#             # SA_interval_range = range(SAFV, SASV + 1)
#
#             if (
#                     FASV in interval_range and SAFV in interval_range
#                     # FASV in SA_interval_range and SAFV in FA_interval_range
#                     # and FASV in interval_range and SAFV in interval_range
#             ):
#                 intervals_copy[i:j+1] = [[FAFV, SASV]]
#
#     intervals_copy = list(set(tuple(i) for i in intervals_copy))
#     if len(intervals_copy) > 1:
#         FAFV, FASV, SAFV, SASV = (
#             intervals_copy[-2][-2],
#             intervals_copy[-2][-1],
#             intervals_copy[-1][-2],
#             intervals_copy[-1][-1],
#         )
#         if FAFV > SAFV:
#             FAFV, SAFV = SAFV, FAFV
#         if FASV > SASV:
#             FASV, SASV = SASV, FASV
#         interval_range = range(FAFV, SASV + 1)
#         FA_interval_range = range(FAFV, FASV + 1)
#         SA_interval_range = range(SAFV, SASV + 1)
#
#         if (
#                 FASV in SA_interval_range and SAFV in FA_interval_range
#                 and FASV in interval_range and SAFV in interval_range
#         ):
#             intervals_copy[-2:] = [[FAFV, SASV]]
#     return intervals_copy


# def merge(self, intervals: List[List[int]]) -> List[List[int]]:  # noqa
#     intervals.sort(key=lambda x: x[0])
#
#     external = []
#     i = 0
#     while i < len(intervals):
#         intervals_copy = []
#         j = i + 1
#         while j < len(intervals):
#             print("consider", intervals[i], intervals[j])
#             FAFV, FASV, SAFV, SASV = (
#                 intervals[i][0],
#                 intervals[i][1],
#                 intervals[j][0],
#                 intervals[j][1],
#             )
#
#             # if FAFV > SAFV:
#             #     FAFV, SAFV = SAFV, FAFV
#             # if FASV > SASV:
#             #     FASV, SASV = SASV, FASV
#             # print(FAFV, SASV)
#             interval_range = range(FAFV, SASV + 1)
#             FA_interval_range = range(FAFV, FASV + 1)
#             SA_interval_range = range(SAFV, SASV + 1)
#
#             if (
#                     FASV in SA_interval_range and SAFV in FA_interval_range and
#                     FASV in interval_range and SAFV in interval_range
#             ):
#                 intervals_copy.append([FAFV, SASV])
#             else:
#                 print("khatam")
#                 break
#             j += 1
#         if intervals_copy:
#             intervals[i:j] = [intervals_copy[-1]]
#             external += [intervals_copy[-1]]
#         else:
#             external.append(intervals[i])
#         i += 1
#         # break
#     print("intervals", intervals)
#     return external
