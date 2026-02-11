class DisjointSet:
    # Constructor
    def __init__(self, n):
        # Resize the arrays
        self.rank = [0] * (n + 1)
        self.parent = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    # Helper function to find ultimate
    # parent along with path compression 
    def findUPar(self, node):
        # Base case
        if node == self.parent[node]:
            return node
        
        # Backtracking step for path compression
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    # Function to determine if two nodes 
    # are in the same component or not
    def find(self, u, v):
        # Return true if both have same ultimate parent 
        return self.findUPar(u) == self.findUPar(v)

    # Function to perform union of 
    # two nodes based on ranks 
    def unionByRank(self, u, v):
        # Get the ultimate parents of both nodes
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        # Return if nodes already belong to the same component
        if ulp_u == ulp_v:
            return

        # Otherwise, join the node to the other 
        # node having higher ranks among the two
        if self.rank[ulp_u] < self.rank[ulp_v]:
            # Update the parent
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            # Update the parent
            self.parent[ulp_v] = ulp_u
        else:
            # Update the parent
            self.parent[ulp_v] = ulp_u
            # Update the rank
            self.rank[ulp_u] += 1

    # Function to perform union of 
    # two nodes based on sizes
    def unionBySize(self, u, v):
        # Get the ultimate parents of both nodes
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        # Return if nodes already belong to the same component
        if ulp_u == ulp_v:
            return

        # Otherwise, join the node belonging to the smaller 
        # component to the node belonging to bigger component
        if self.size[ulp_u] < self.size[ulp_v]:
            # Update the parent
            self.parent[ulp_u] = ulp_v
            # Update the size 
            self.size[ulp_v] += self.size[ulp_u]
        else:
            # Update the parent
            self.parent[ulp_v] = ulp_u
            # Update the size
            self.size[ulp_u] += self.size[ulp_v]

if __name__ == "__main__":
    # Disjoint Data structure
    ds = DisjointSet(7)
    ds.unionByRank(1, 2) # Adding edge between 1 and 2
    ds.unionByRank(2, 3) # Adding edge between 2 and 3
    ds.unionByRank(4, 5) # Adding edge between 4 and 5
    ds.unionByRank(6, 7) # Adding edge between 6 and 7
    ds.unionByRank(5, 6) # Adding edge between 5 and 6

    # Checking if node 3 and node 7 
    # are in the same component
    if ds.find(3, 7):
        print("They belong to the same components.")
    else:
        print("They do not belong to the same components.")

    ds.unionByRank(3, 7) # Adding edge between 3 and 7

    # Checking again if node 3 and node 7 
    # are in the same component
    if ds.find(3, 7):
        print("They belong to the same components.")
    else:
        print("They do not belong to the same components.")
