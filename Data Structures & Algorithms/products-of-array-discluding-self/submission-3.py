class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_forward = []
        prod_backward = []
        prod = 1
        for n in nums:
            prod *= n
            prod_forward.append(prod)
        prod = 1
        for n in reversed(nums):
            prod *= n
            prod_backward.insert(0, prod)
        ans = []
        for idx, n in enumerate(nums):
            a = 1
            if idx - 1 >= 0:
                a *= prod_forward[idx-1]
            if idx + 1 < len(nums):
                a *= prod_backward[idx+1]
            ans.append(a)
        return ans
            