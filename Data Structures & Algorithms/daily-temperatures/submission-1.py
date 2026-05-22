class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stk = []
        for idx, t in enumerate(temperatures):
            if not stk:
                stk.append((t, idx))
                continue
            
            while stk and t > stk[-1][0]:
                popped = stk.pop()
                ans[popped[1]] = (idx - popped[1])

            stk.append((t,idx))

            # print(stk)

        return ans