class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums)
        ans = 0
        for n in nums:
            if n - 1 not in uniq:
                run = 0
                while n in uniq:
                    run += 1
                    n += 1
                    ans = max(ans, run)
        return ans