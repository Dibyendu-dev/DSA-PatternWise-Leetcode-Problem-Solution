
import heapq

def spanning_tree(self,V,adj):
    pq = []
    visited = [False] * V
    heapq.heappush(pq, (0, 0))
    sum = 0
    while pq:
        wt, node = heapq.heappop(pq)
        if visited[node]:
            continue
        visited[node] = True
        sum += wt
        for it in adj[node]:
            adjNode = it[0]
            edgeWt = it[1]
            if visited[adjNode] == 0:
                heapq.heappush(pq, (edgeWt, adjNode))
    return sum