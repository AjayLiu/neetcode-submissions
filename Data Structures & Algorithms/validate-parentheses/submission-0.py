class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {'(':')','[':']', '{':'}'}
        stk = []
        for c in s:
            if c in openToClose.keys():
                stk.append(c)
            if c in openToClose.values():
                if len(stk) == 0 or openToClose[stk.pop()] != c:
                    return False
        
        return len(stk) == 0