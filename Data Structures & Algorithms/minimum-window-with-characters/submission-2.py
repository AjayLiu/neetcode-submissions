from collections import Counter
class Solution:
    def isValidWindow(self, wnd: str, t: str) -> bool:
        # print(wnd, "vs", t)
        wndFreq = Counter(wnd)
        tFreq = Counter(t)
        return tFreq <= wndFreq
        

    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if t == s:
            return s

        bestwnd = s
        wnd = ""
        found = False
        for i in range(len(t)):
            wnd += s[i]

        l = 0
        r = len(wnd)
        while r <= len(s):
            wnd = s[l:r]
            # print(wnd)
            # If window is valid, try shrinking window from left side
            if self.isValidWindow(wnd, t):
                # print("FOUND " + wnd)
                found = True
                if len(wnd) < len(bestwnd):
                    bestwnd = wnd
                l += 1
            else:
                r += 1
        
        if not found:
            return ""
            
        return bestwnd