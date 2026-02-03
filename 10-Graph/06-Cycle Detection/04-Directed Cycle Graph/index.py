class Solution:
    def dfs(self,adj,u,visited,recStack):
        if recStack[u]:
            return True
        if visited[u]:
            return False
        visited[u] = True
        recStack[u] = True
        
        for v in adj[u]:
            if self.dfs(adj,v,visited,recStack):
                return True
        
        recStack[u] = False
        return False
    
    def isCyclic(self, V, edges):
        # code here
        adj = [[] for _ in range(V)]
        
        for u, v in edges:
            adj[u].append(v)
        visited = [False] * V
        recStack = [False] * V
        
        for i in range(V):
            if not visited[i] and self.dfs(adj,i,visited,recStack):
                return True
        return False