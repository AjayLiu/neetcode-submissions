class Solution:
    def dfs(self, i: int, j: int, grid: List[List[int]], dist: int) -> None:
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == -1:
            return
        if grid[i][j] == 0 or dist < grid[i][j]:
            grid[i][j] = min(grid[i][j],dist)
            self.dfs(i+1, j, grid, dist + 1)
            self.dfs(i-1, j, grid, dist + 1)
            self.dfs(i, j-1, grid, dist + 1)
            self.dfs(i, j+1, grid, dist + 1)
        
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    self.dfs(i, j, grid, 0)