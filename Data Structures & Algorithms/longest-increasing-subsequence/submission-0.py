class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # DP(i) = length of longest subsequence up to nums[i]
        # DP(i) = max(include i, dont include i)
        # include i = 1 + DP(j) if j nums[j] < nums[i]
        # dont include i = 1

        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            best = 1
            for j in range(0, i):
                if nums[j] < nums[i]:
                    best = max(best, 1 + dp[j])
            dp[i] = best
        return max(dp)
