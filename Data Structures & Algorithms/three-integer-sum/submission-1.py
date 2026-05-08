class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i, n in enumerate(nums):

            # skip duplicate fixed numbers
            if i > 0 and n == nums[i - 1]:
                continue

            j, k = i + 1, len(nums) - 1

            while j < k:
                total = n + nums[j] + nums[k]

                if total < 0:
                    j += 1

                elif total > 0:
                    k -= 1

                else:
                    ans.append([n, nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # skip duplicate left values
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # skip duplicate right values
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return ans