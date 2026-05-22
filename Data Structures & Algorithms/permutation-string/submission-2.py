from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Freq = Counter(s1)
        freq = [0] * 26
        l, r = 0, 0
        while r < len(s2):
            cr = s2[r]
            cl = s2[l]
            freq[ord(cr) - ord('a')] += 1

            w = r - l
            if w >= len(s1):
                print("DEL " + cl)
                freq[ord(cl) - ord('a')] -= 1
                l += 1
            
            print("w = " + s2[l:r+1])
            print(freq)
            
            good = True
            for c in s1:
                if freq[ord(c) - ord('a')] < s1Freq[c]:
                    good = False
                    break
            if good:
                return True
            r += 1
        return False
            


           
        