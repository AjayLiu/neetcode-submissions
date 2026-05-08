class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for idx in range(len(s)):
            c = s[idx]

            left, right = idx - 1, idx + 1
            # odd
            while(left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
                ans += 1

            # even
            left, right = idx, idx + 1
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                left -= 1
                right += 1
                ans += 1
        return ans + len(s)