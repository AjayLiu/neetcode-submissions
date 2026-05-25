class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        def dfs(sumSoFar: int, idx: int):
            if idx >= len(nums):
                return False
            if sumSoFar == sum(nums) // 2:
                return True
            return dfs(sumSoFar + nums[idx], idx + 1) or dfs(sumSoFar, idx + 1)
        
        return dfs(0, 0)