from collections import deque

def isCyclic(adj):
    v = len(adj)

    indegree = [0] * v   #compute indegree
    for u in range(v):
        for v in adj[u]:
            indegree[v] +=1

    q = deque()         # push nodes in-degree 0
    for i in range(v):
        if indegree[i] == 0:
            q.append(i)
    
    topo_order = []

    while q:             # implement bfs
        u = q.popleft()
        topo_order.append(u)

        for v in adj[u]:
            indegree[v] -=1
            if indegree[v] == 0:
                q.append(v)
        
    if len(topo_order) != v:
        return True
    return False
            