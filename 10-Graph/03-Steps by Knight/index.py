from collections import deque
class Solution:
    
    def isValid(self, i,j,n,visited):
        return 0<= i < n and 0<= j < n  and not visited[i][j]
    
    def minStepToReachTarget(self, knightPos, targetPos, n):
        
        N=n
        tx,ty=targetPos[0]-1,targetPos[1]-1
        x1,y1= knightPos[0]-1,knightPos[1]-1
        
        if x1==tx and y1==ty:
            return 0
        
        visited = [[False]*n for _ in range(n)]
        
        # bfs 
        
        q=deque()
        q.append((x1,y1))
        visited[x1][y1]=True
        
        moves = [
            (1,2),(1,-2),(-1,2),(-1,-2),
            (2,1),(2,-1),(-2,1),(-2,-1)
            ]
            
        steps =0
        
        while q:
            level_size = len(q)
            steps += 1
            
            for _ in range(level_size):
                x,y=q.popleft()
                
                for dx,dy in moves:
                    nx , ny = x+dx, y+dy
                    
                    if nx == tx and ny == ty:
                        return steps
                    
                    if self.isValid(nx,ny,n,visited):
                        visited[nx][ny]=True
                        q.append((nx,ny))
                        
        return steps