import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [((p[0])**2 + (p[1])**2, p) for p in points]
        heapq.heapify(heap)
        ans = []
        for _ in range(k):
            p = heapq.heappop(heap)
            ans.append(p[1])
        return ans