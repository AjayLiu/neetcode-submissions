class Solution {
public:
    int search(vector<int>& nums, int target) {
        auto iter = lower_bound(nums.begin(), nums.end(), target);
        if (binary_search(nums.begin(), nums.end(), target)){
            return iter - nums.begin();
        }
        return -1;
    }
};
