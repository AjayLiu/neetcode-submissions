class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        best = 0
        exists = set(nums)
        for n in nums:
            streak = 1
            if n-1 not in exists:
                while n+1 in exists:
                    n += 1
                    streak += 1
            best = max(best, streak)
        return best
            