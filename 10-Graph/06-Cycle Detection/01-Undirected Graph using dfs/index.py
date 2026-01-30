def dfs(v,adj,visited,parent):
    visited[v] = True

    for neighbor in adj[v]:
        if not visited[neighbor]:
            if dfs(neighbor,adj,visited,v):
                return True
        elif neighbor != parent:
            return True    
    
    return False

def iscycle(adj):
    V = len(adj)
    visited = [False] * V

    for u in range(V):
        if not visited[u]:
            if dfs(u,adj,visited,-1):
                return True
    
    return False