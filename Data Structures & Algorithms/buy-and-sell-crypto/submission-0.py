class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        left = 0
        right = 1
        while(left < len(prices) - 1):
            if prices[left+1] < prices[left]:
                left += 1
                continue
            right = left + 1
            while right < len(prices):
                profit = prices[right] - prices[left]
                best = max(best, profit)
                right += 1
            left += 1
        
        return best