from collections import defaultdict

def topological_sort(self, node, adj, visited, st):
   visited[node] = True
   for neighbor, wt in adj[node]:
      if not visited[neighbor]:
         topological_sort(neighbor, adj, visited, st)

   st.append(node)

def shortestpath(self, N ,M, edges):
   adj = defaultdict(list)
   for u, v, wt in edges:
      adj[u].append((v, wt))

   visited = [False] * N
   st = []
   for i in range(N):
      if not visited[i]:
         topological_sort(i, adj, visited, st)

   dist = [1e9] * N
   dist[0] = 0
   while st:
      node = st.pop()
      for neighbor, wt in adj[node]:
         if dist[node] + wt < dist[neighbor]:
            dist[neighbor] = dist[node] + wt

      for i in range(N):
         if dist[i] == 1e9:
            dist[i] = -1

   return dist
      
    
    