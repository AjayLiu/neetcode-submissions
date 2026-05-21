from collections import defaultdict, Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 1
        ans = 0
        while r <= len(s): 
            wnd = s[l:r]
            # print(wnd)
            freq = Counter(wnd)
            _ , mostFreqCnt = freq.most_common(1)[0]
            if len(wnd) - mostFreqCnt <= k:
                ans = max(ans, len(wnd))
                r += 1
            else:
                l += 1
        return ans