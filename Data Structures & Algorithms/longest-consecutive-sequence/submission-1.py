class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        exists = set()
        for n in nums:
            exists.add(n)
        
        ans = 0
        for n in nums:
            if n-1 not in exists:
                counter = n
                while counter in exists:
                    counter += 1
                ans = max(counter - n, ans) 
        
        return ans
