from collections import deque
from typing import List
class Solution:
    def topoSort(self,v,adj):
        indegree = [0] * v

        for i in range(v):
            for it in adj[i]:
                indegree[it] +=1

        ans = []
        q = deque()
        for i in range(v):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            node =q.popleft()
            ans.append(node)

            for it in adj[node]:
                indegree[it] -=1
                if indegree[it] == 0:
                    q.append(it)
        return ans



    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses

        adj = [[] for _ in range(n)]
        for it in prerequisites:
            u = it[0]
            v = it[1]

            adj[v].append(u)
            topo =self.topoSort(n,adj)

            if len(topo) < n:
                return False
        return True
        