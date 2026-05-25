class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # DP(i) = (neg, pos) where neg / pos is most negative / positive product so far
        # DP(i) = max(nums[i], dp[i-1][neg] * nums[i], dp[i-1][pos] * nums[i])

        dp = [(n,n) for n in nums]
        for i in range(1, len(nums)):
            neg, pos = dp[i-1]
            most_neg = min(nums[i], pos * nums[i], neg * nums[i])
            most_pos = max(nums[i], pos * nums[i], neg * nums[i])
            dp[i] = (most_neg, most_pos)
            # print(dp)

        return max([dp[i][1] for i in range(0, len(nums))])
