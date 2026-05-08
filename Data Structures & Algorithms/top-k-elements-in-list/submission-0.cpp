class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> freq;
        for(int n : nums){
            freq[n]++;
        }

        vector<vector<int>> buckets (nums.size()+1);
        for(auto iter = freq.begin(); iter != freq.end(); iter++){
            buckets[iter->second].push_back(iter->first);
        }

        vector<int> ans;
        while(k > 0){
            for(int i = nums.size(); i > 0; i--){
                int j = 0;
                while(j < buckets[i].size() && k > 0){
                    ans.push_back(buckets[i][j]);
                    j++;
                    k--;
                }
            }
        }

        return ans;
        
    }
};
