class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # DP[a] = num distinct combinations that sum to a
        dp = [0] * (amount + 1)
        dp[0] = 1

        for c in coins:
            for a in range(c, amount + 1):
                dp[a] += dp[a-c]

        return dp[amount]