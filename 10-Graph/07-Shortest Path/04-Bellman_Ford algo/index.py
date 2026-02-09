def bellmanford(V,edge,src):
    dist = [int(1e9)] * V
    dist[src] = 0

    for i in range(V):
        for u,v,wt in edge:
            if dist[u] != int(1e9) and dist[u] + wt < dist[v]:
                if i == V-1:
                    return [-1]
                dist[v] = dist[u] + wt
    return dist