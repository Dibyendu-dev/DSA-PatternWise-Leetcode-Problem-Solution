
from collections import deque

def bfs(self, src, adj, dist):
    q = deque()
    q.append(src)
    dist[src] = 0

    while q:
        node = q.popleft()

        for neighbor in adj[node]:
            if dist[node] + 1 < dist[neighbor]:
                dist[neighbor] = dist[node] + 1
                q.append(neighbor)
                
def shortestedpath(self,edges,N,M):
    from collections import defaultdict, deque
    
    adj = [[] for _ in range(N)]        

    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    dist = [-1] * N
    self.bfs(0, adj, dist)

    for i in range(N):
        if dist[i] == float('inf'):
            dist[i] = -1
    
    return dist