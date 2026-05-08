class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums[0]]
        
        runningProduct = []

        prod = 1
        for n in nums:
            prod *= n
            runningProduct.append(prod)
        
        backwardsProduct = []
        prod = 1
        for n in reversed(nums):
            prod *= n
            backwardsProduct.insert(0, prod)
        
        ans = []
        ans.append(backwardsProduct[1])
        for i in range(1, len(nums)-1):
            ans.append(runningProduct[i-1] * backwardsProduct[i+1])
        ans.append(runningProduct[-2])
        return ans