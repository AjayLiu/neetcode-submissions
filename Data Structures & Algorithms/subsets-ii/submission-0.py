class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def dfs(run:List[int], idx:int):
            if idx == len(nums):
                ans.append(run)
                return

            n = nums[idx]
            dfs(run + [n], idx + 1)

            unique_idx = idx + 1
            while unique_idx < len(nums) and nums[unique_idx] == n:
                unique_idx += 1
            dfs(run, unique_idx)

        dfs([], 0)
        return ans