class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        ans = 0
        l = 0
        for idx, c in enumerate(s):
            if c in seen:
                while s[l] != c:
                    if s[l] in seen:
                        seen.remove(s[l])
                    l += 1
                l += 1
            seen.add(c)
            # print(idx - l + 1)
            ans = max(ans, idx - l + 1)



        return ans

