from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int) # {number: freq}
        for n in nums:
            freq[n] += 1

        maxHeap = [(-count, num) for num, count in freq.items()]
        heapq.heapify(maxHeap)

        ans = []
        for _ in range(k):
            negcount, num = heapq.heappop(maxHeap)
            ans.append(num)
        return ans
