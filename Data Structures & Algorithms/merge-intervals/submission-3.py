class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        ans = []
        idx = 0
        while idx < len(intervals):
            begin, end = intervals[idx]
            while idx < len(intervals) and intervals[idx][0] <= end:
                # print((begin, end), "collides with ", intervals[idx])
                end = max(end, intervals[idx][1])
                idx += 1
            ans.append([begin, end])

        return ans