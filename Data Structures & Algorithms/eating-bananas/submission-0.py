class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        best = max(piles)
        while left < right:
            k = left + (right - left) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            # print("k= ", k, ", h= ", hours)
            if hours > h:
                left = k + 1
            else:
                right = k
                best = min(best, k)
        return best