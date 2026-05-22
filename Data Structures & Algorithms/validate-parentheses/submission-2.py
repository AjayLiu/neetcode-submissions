class Solution:
    def isValid(self, s: str) -> bool:
        openToClose = {
            '{': '}',
            '(': ')',
            '[': ']'
        }

        stk = []
        for c in s:
            if c in openToClose.values():
                if not stk:
                    return False
                if c != openToClose[stk[-1]]:
                    return False
                stk.pop()
            else:
                stk.append(c)
        return len(stk) == 0
