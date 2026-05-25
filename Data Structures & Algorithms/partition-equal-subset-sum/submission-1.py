class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        
        half = sum(nums) // 2
        dp = [([None] * (1 + half)) for _ in range(len(nums))]

        def dfs(sumSoFar: int, idx: int) -> bool:
            if idx >= len(nums) or sumSoFar > half:
                return False
            if sumSoFar == half:
                return True
            
            if dp[idx][sumSoFar]:
                return dp[idx][sumSoFar]
            
            dp[idx][sumSoFar] = dfs(sumSoFar + nums[idx], idx + 1) \
                or dfs(sumSoFar, idx + 1)

            return dp[idx][sumSoFar]
        
        return dfs(0, 0)