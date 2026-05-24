class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(soFar: List[int], idx: int, remaining: int):
            if remaining < 0 or idx >= len(nums):
                return

            n = nums[idx]

            dfs(soFar + [n], idx, remaining - n)
            dfs(soFar, idx + 1, remaining)
            
            if n == remaining:
                ans.append(soFar + [n])
                return
        
        dfs([], 0, target)
        return ans