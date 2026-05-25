class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def dfs(running: List[int], picked: List[bool]):
            # print(running)
            # print(picked)
            # print("***")
            
            if len(running) == len(nums):
                ans.append(running)
                return

            for i in range(len(nums)):
                if not picked[i]:
                    picked[i] = True
                    dfs(running + [nums[i]], picked)
                    picked[i] = False
            
        dfs([], [False] * len(nums))
        return ans