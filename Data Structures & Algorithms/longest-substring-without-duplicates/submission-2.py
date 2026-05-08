class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        longest = 0
        thisLen = 0
        for c in s:
            thisLen += 1
            while c in seen: 
                seen.remove(s[left])
                left += 1
                thisLen -= 1
            seen.add(c)
            longest = max(longest, thisLen)
        return longest
            