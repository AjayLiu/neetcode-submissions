class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l = 0
        best = 0
        for r in range(len(s)):
            c = s[r]
            if c in seen:
                while s[l] != c:
                    if s[l] in seen:
                        seen.remove(s[l])
                    l += 1
                seen.remove(c)
                l += 1
            seen.add(c)
            # print(s[l:r+1])
            # print(seen)
            best = max(best, r - l + 1)
        return best

            