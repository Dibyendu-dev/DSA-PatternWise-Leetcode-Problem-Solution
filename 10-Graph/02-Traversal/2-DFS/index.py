class Solution:
    def dfsRec(self,adj,vis,s,res):
        vis[s]= True
        res.append(s)
        for i in adj[s]:
            if not vis[i]:
                self.dfsRec(adj,vis,i,res)
        
    def dfs(self, adj):
        # code here
        vis = [False]*len(adj)
        res = []
        self.dfsRec(adj,vis,0,res)
        return res