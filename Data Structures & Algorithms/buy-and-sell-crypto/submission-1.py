class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minSoFar = prices[0]
        best = 0
        for idx, p in enumerate(prices[1:]):
            best = max(best, p - minSoFar)
            minSoFar = min(minSoFar, p)
        return best
            
