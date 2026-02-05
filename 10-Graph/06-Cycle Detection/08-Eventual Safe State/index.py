from collections import deque

def eventualSafeNodes(v,adj):
    adjRev = [[] for _ in range(v) ]
    indegree = [0] * v

    for i in range(v):
        for neighbor in adj[i]:
            adjRev[neighbor].append(i)
            indegree[i] +=1
    
    safeNodes = []
    q = deque()
    for i in range(v):
        if indegree[i] == 0:
            q.append(i)
        
    while q:
        node =q.popleft()
        safeNodes.append(node)

        for parent in adjRev[node]:
            indegree[parent] -=1
            if indegree[parent] == 0:
                q.append(parent)
    safeNodes.sort()
    return safeNodes

            