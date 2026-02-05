from typing import List

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]

        for a, b in connections:
            graph[a].append((b,1))
            graph[b].append((a,0))

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            changes = 0

            for neighbor,cost in graph[node]:
                if not visited[neighbor]:
                    changes += cost
                    changes += dfs(neighbor)
                
            return changes

        return dfs(0)