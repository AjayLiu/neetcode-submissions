import bisect
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = []
        for row in matrix:
            flat.extend(row)
        idx = bisect.bisect_left(flat, target)
        return (not idx >= len(flat)) and flat[idx] == target