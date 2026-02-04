from collections import deque

def topoSort(adj):
    n = len(adj)
    indegree = [0] * n
    res = []
    q = deque()

    for i in range(n):
        for next_node in adj[i]:
            indegree[next_node] +=1

    for i in range(n):
        if indegree[i] == 0:
            q.append(i)

    while q:
        top = q.popleft()
        res.append(top)
        for next_node in adj[top]:
            indegree[next_node] -=1
            if indegree[next_node] == 0:
                q.append(next_node)
    if len(res) != n:
        return []
    return res

def built_adjList(V,edges):
    adj = [[] for _ in range(V)]
    for u, v in edges:
        adj[u].append(v)
    return adj

