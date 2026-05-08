class Solution:
    def dfs(self, grid: list[list[int]], i: int, j: int) -> int:
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
            return 0
        if i == len(grid)-1 or j == len(grid[i])-1:
            return 1
        
        return self.dfs(grid, i+1, j) + self.dfs(grid, i, j+1)
        


    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0]*n for _ in range(m)]
        return self.dfs(grid, 0,0)