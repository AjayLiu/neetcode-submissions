class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        run = []
        def dfs(used):
            # print(run)
            if len(run) == len(nums):
                ans.add(tuple(run[:]))
                return
            
            if all(used):
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                run.append(nums[i])
                dfs(used[:])
                used[i] = False
                run.pop()

        dfs([False] * len(nums))
        return list(ans)