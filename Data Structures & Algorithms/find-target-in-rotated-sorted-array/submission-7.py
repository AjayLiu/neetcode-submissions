class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            
            # Normal right side
            if nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m
            else:
                if nums[l] <= target < nums[m]:
                    r = m
                else:
                    l = m + 1

        if nums[l] == target:
            return l
        return -1