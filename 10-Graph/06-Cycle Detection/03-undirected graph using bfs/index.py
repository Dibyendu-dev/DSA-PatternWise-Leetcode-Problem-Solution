from collections import deque

def bfs(start,adj,visited):
    q= deque([start,-1])
    visited[start] = True
    while q:
        node, parent = q.popleft()

        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor]= True
                q.append((neighbor,node))
            elif neighbor != parent:
                return True
        return False



def isCycle(V,edges):
    adj = [[] for _ in range(V)]

    for u,v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    visited = [False] * V

    for i in range(V):
        if not visited[i]:
            if bfs(i,adj,visited):
                return True
            
    return False
