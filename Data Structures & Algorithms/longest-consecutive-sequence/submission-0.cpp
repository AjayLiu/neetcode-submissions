class Solution {
public:
    int longestConsecutive(vector<int>& nums){

        // Store numbers is set
        unordered_set<int> seen;
        for(int num : nums){
            seen.insert(num);
        }

        int longestLengthSequence = 0;
        for(int num : nums){
            // If this number is beginning of sequence (no left neighbor)
            int counter = 0;
            if(seen.find(num-1) == seen.end()){
                while(seen.find(num + counter) != seen.end()){
                    counter++;
                }
            }

            longestLengthSequence = max(longestLengthSequence, counter);
        }

        return longestLengthSequence;
    }
};
