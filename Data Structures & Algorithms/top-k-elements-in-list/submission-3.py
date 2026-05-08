from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        for key, count in Counter(nums).items():
            freq[count].append(key)
        
        ans = []
        i = len(freq) - 1
        while len(ans) < k:
            ans += freq[i]
            i -= 1
        return ans[:k]


