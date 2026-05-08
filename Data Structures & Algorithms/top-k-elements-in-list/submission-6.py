from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums)+1)] 
        counter = Counter()
        for key, v in counter.items():
            buckets[v].append(key)
        
        buckets = [[] for _ in range(len(nums)+1)] 
        counter = Counter(nums)
        for key, v in counter.items():
            buckets[v].append(key)

        res = []
        for bucket in reversed(buckets):
            res.extend(bucket)
            if len(res) >= k:
                return res[:k]

        # return [k for k,v in Counter(nums).most_common(k)]

        # return [k for k,v in Counter(nums).most_common(k)]
        
        
