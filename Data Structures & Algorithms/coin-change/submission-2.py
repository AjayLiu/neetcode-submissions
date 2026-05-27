class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # DP[i] = min number of coins needed to make i
        # DP[i] = min(1 + DP[i-c]) for all c in coins
        # len(DP) = amount + 1
        # Each DP[i] takes c runs so runtime is O(amount * coins)

        if amount == 0:
            return 0

        dp = [-1] * (amount+1)
        for c in coins:
            if c > amount:
                continue
            dp[c] = 1

        for i in range(1, amount + 1):
            if dp[i] == 1:
                continue
            best = amount
            for c in coins:
                idx = i - c
                if idx >= 0 and idx < len(dp) and dp[idx] != -1:
                    dp[i] = min(best, 1 + dp[idx])
                    best = dp[i]

        return dp[amount]
