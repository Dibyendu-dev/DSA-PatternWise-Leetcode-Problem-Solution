from typing import List

class Solution:
    def get_directions(self):
        return [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def in_bounds(self, r, c):
        return 0 <= r < self.rows and 0 <= c < self.cols

    def dfs(self, r, c, pr, pc):
        self.visited[r][c] = True

        for dr, dc in self.get_directions():
            nr, nc = r + dr, c + dc

            if not self.in_bounds(nr, nc):
                continue

            if self.grid[nr][nc] != self.grid[r][c]:
                continue

            if not self.visited[nr][nc]:
                if self.dfs(nr, nc, r, c):
                    return True
            elif (nr, nc) != (pr, pc):
                return True

        return False

        
    def containsCycle(self, grid: List[List[str]]) -> bool:
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.grid = grid
        self.visited = [[False] * self.cols for _ in range(self.rows)]

        for r in range(self.rows):
            for c in range(self.cols):
                if not self.visited[r][c]:
                    if self.dfs(r, c, -1, -1):
                        return True
        return False
        