import math
from functools import reduce
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        biggest_pile = max(piles)
        l = 1
        r = biggest_pile
        min_k = r
        while l < r:
            k = l + (r - l) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            if hours <= h:
                min_k = min(min_k, k)
                r = k
            else:
                l = k + 1
        return min_k