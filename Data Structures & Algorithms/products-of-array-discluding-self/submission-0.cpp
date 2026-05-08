class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        size_t n = nums.size();
        vector<int> prefix(n), suffix(n), ans(n);

        int prefixProduct = 1;
        for(size_t i = 0; i < n; i++){
            prefixProduct *= nums[i];
            prefix[i]=prefixProduct;
        }

        int suffixProduct = 1;
        for(int i = n-1; i >= 0; i--){
            suffixProduct *= nums[i];
            suffix[i] = suffixProduct;
        }

        for(size_t i = 0; i < n; i++){
            int value = 1;
            if(i > 0){
                value *= prefix[i-1];
            }
            if(i < n - 1){
                value *= suffix[i+1];
            }
            ans[i] = value;
        }

        return ans;
    }
};
