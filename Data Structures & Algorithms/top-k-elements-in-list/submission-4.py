from collections import Counter, defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = defaultdict(list)
        for item, count in counter.items():
            freq[count].append(item)

        ans = []
        for freq, item in reversed(sorted(freq.items())):
            ans += item
            if len(ans) >= k:
                return ans[:k]
        