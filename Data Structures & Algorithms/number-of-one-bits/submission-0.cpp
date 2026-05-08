class Solution {
public:
    int hammingWeight(uint32_t n) {
        int weight = 0;
        while(n != 0){
            if(n & 1 == 1){
                weight ++;
            }
            n = n >> 1;
        }
        return weight;
    }
};
