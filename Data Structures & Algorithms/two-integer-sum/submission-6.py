class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = dict()
        for idx, n in enumerate(nums):
            if n in comp:
                return sorted([idx, comp[n]])
            comp[target - n] = idx
        return -1