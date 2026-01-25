def createGraph(V,edges):
    adj= [[] for _ in range(V)]

    for it in edges:
        u = it[0]
        v = it[1]
        adj[u].append(v)
        
    return adj

if __name__ == "__main__":
    v=3
    edges=[[1,0],[1,2],[2,0]]

    adj = createGraph(v,edges)

    print("adjacency matrix representattion of undirected graph")
    for i in range(v):
        print(f"{i}:",end=" ")
        for j in adj[i]:
            print(j,end=" ")
        print()
            


