class Solution {
public:

    string longestLengthPalindromeCenteredAt(string s, int center){

        // Odd length palindrome case
        int left = center - 1;
        int right = center + 1;
        string oddPalindrome = string(1,s[center]);
        while(left >= 0 && right < s.size()){
            if(s[left] != s[right]){
                break;
            }
            oddPalindrome.insert(0, string(1,s[left]));
            oddPalindrome += s[right];
            left--;
            right++;
        }

        // Even length palindrome case
        left = center;
        right = center + 1;
        string evenPalindrome = "";
        while(left >= 0 && right < s.size()){
            if(s[left] != s[right]){
                break;
            }
            evenPalindrome.insert(0, string(1,s[left]));
            evenPalindrome += s[right];
            left--;
            right++;
        }

        // cout << "odd " << oddPalindrome << endl;
        // cout << "even " << evenPalindrome << endl;
        
        return oddPalindrome.size() > evenPalindrome.size() ? oddPalindrome : evenPalindrome;
    }
    string longestPalindrome(string s) {
        string longest = "";
        for(int i = 0; i < s.size(); i++){
            string palin = longestLengthPalindromeCenteredAt(s, i);
            if(palin.size() > longest.size()) {
                longest = palin;
            }
        }
        return longest;
    }
};
