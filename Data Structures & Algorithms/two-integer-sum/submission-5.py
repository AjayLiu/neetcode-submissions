class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {} # maps {complement: index}
        # [3, 2, 5, 7]
        # if target is 10
        # 3 is complement for 7 at index 0
        # complement[7] = 0
        for i, n in enumerate(nums):
            comp = target - n
            if n in complement:
                return sorted([i, complement[n]])
            complement[comp] = i