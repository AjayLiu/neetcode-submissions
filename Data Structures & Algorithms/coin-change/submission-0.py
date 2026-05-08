class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10001] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        # DP[a] = Number of coins needed to get a
        for a in range(amount+1):
            for coin in coins:
                if a-coin >= 0:
                    dp[a] = min(dp[a], 1+dp[a-coin])
        
        print (dp)
        if dp[amount] == 10001:
            return -1
        return dp[amount]
        