class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        run = []
        def dfs(i):
            if len(run) == k:
                ans.append(run[:])
                return
            
            for j in range(i, n + 1):
                run.append(j)
                dfs(j + 1)
                run.pop()
        
        dfs(1)
            
        return ans