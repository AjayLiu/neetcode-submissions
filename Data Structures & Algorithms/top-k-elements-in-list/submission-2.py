from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        # buckets = {frequency : [items]}
        buckets = defaultdict(list)
        for item, freq in freq.items():
            buckets[freq].append(item)
        
        ans = []
        for f in sorted(buckets.keys(), reverse=True):
            for item in buckets[f]:
                ans.append(item)
            if len(ans) == k:
                return ans
            
