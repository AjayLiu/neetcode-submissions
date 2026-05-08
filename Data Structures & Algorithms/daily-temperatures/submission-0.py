class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        ans = [0] * len(temperatures)
        for idx, temp in enumerate(temperatures):
            while stk and temp > stk[-1][0]:
                t, i = stk.pop()
                ans[i] = idx - i

            stk.append((temp, idx))
        return ans