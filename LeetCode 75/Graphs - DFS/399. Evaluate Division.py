"""You are given an array of variable pairs equations and an array of real numbers values, where
equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that
represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the
answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero
and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined
for them.

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0],
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined => -1.0

Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0],
queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits."""
from collections import defaultdict, deque
from typing import List


class Solution:

    def calcEquation(  # noqa
            self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        adj_list = defaultdict(list)
        for idx, equation in enumerate(equations):
            a, b = equation
            adj_list[a].append([b, values[idx]])
            adj_list[b].append([a, 1 / values[idx]])

        def dfs(src, target):
            if src not in adj_list or target not in adj_list:
                return -1

            q, visit = deque(), set()
            q.append([src, 1])
            visit.add(src)
            while q:
                n, w = q.popleft()
                if n == target:
                    return w
                for nei, weight in adj_list[n]:
                    if nei not in visit:
                        q.append([nei, weight * w])
                        visit.add(nei)
            return -1

        return [dfs(query[0], query[1]) for query in queries]

    def calcEquation2(  # noqa
            self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        adj_list = {}
        hash_map = {}
        for idx, arr in enumerate(equations):
            first, second = arr
            hash_map[first + "/" + second] = values[idx]
            if first not in adj_list:
                adj_list[first] = []
            if second not in adj_list:
                adj_list[second] = []
            adj_list[first].append((values[idx], second))

        for key, value in adj_list.items():
            for idx1, val1 in value:
                for idx2, val2 in adj_list[val1]:
                    mul = idx1 * idx2
                    hash_map[key + "/" + val2] = mul
                    adj_list[key].append((mul, val2))

        res = []
        for q, u in queries:
            key = q + "/" + u
            if q == u and q in adj_list:
                val = 1
            elif key in hash_map:
                val = hash_map.get(key, -1)
            else:
                val = 1 / hash_map.get(u + "/" + q, -1)
            res.append(val)

        print(dict(sorted(hash_map.items())))
        print(adj_list)
        return res


if __name__ == '__main__':
    print(Solution().calcEquation(
        [["a", "b"], ["b", "c"], ["c", "d"]],
        [2.0, 3.0, 5.0],
        [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"], ["b", "d"], ["a", "d"]]
    ))
