class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def recurse(i: int, target: int, currList: List[int]):
            if sum(currList) > target or i >= len(nums):
                return
            if sum(currList) == target:
                ans.append(currList)
                return
            
            num = nums[i]
            # Use this num
            newList = currList[:]
            newList.append(num)
            recurse(i, target, newList)

            # Don't use this num, also exclude it from future use
            recurse(i + 1, target, currList.copy())

        recurse(0, target, [])
        return ans
