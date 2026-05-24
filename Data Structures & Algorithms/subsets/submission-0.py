class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(soFar, idx):
            if idx == len(nums):
                ans.append(soFar)
                return
            
            dont_include = dfs(soFar, idx + 1)
            include = dfs(soFar + [nums[idx]], idx + 1)
        
        dfs([], 0)
        return ans
        