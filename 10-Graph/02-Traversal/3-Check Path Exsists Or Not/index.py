class Solution:
    def dfs(self,visited,adj,source):
        visited[source] = 1
        for neighbour in adj[source]:
            if not visited[neighbour]:
                self.dfs(visited,adj,neighbour)
       
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        visited = [0] * n

        adj= [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        self.dfs(visited,adj,source)
        return visited[destination] == 1
        