class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        i = 0
        n = len(intervals)

        start, end = newInterval

        # All intervals before newInterval
        # iiiiii
        #         nnnnnn
        while i < n and intervals[i][1] < start:
            ans.append(intervals[i])
            i += 1
        
        # While overlapped
        #        iiiiiii 
        #  nnnnnnnn
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        ans.append([start, end])

        # All interval after newInterval
        #          iiiiiii
        # nnnnnnn
        while i < n and intervals[i][0] > end:
            ans.append(intervals[i])
            i += 1

        return ans

