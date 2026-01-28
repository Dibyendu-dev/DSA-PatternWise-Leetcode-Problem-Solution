from typing import List
class Solution:

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        visited = [False] * n

        def dfs(city):
            for neighbour in range(n):
                if isConnected[city][neighbour] ==1 and not visited[neighbour]:
                    visited[neighbour] = True
                    dfs(neighbour)

        provinces = 0
        for i in range(n):
            if not visited[i]:
                provinces +=1
                dfs(i)
        return provinces
         