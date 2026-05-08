class Solution {
public:

    vector<string> combos(string digits, map<char, vector<string>> &digitToLetters){
        cout << "FIND COMBO " << digits << endl;
        if(digits.size() == 0){
            return {};
        }
        if(digits.size() == 1){
            return digitToLetters[digits[0]];
        }
        vector<string> ans;
        // Get combos of everything except first char
        vector<string> combosSuffix = combos(digits.substr(1, digits.size()-1), digitToLetters);

        vector<string> letters = digitToLetters[digits[0]];
        for(string letter: letters){
            for(int i = 0; i < combosSuffix.size(); i++){
                ans.push_back(letter + combosSuffix[i]);
                cout << ans[i] << endl;
            }
        }

        return ans;
    }

    vector<string> letterCombinations(string digits) {
        vector<string> ans;

        map<char, vector<string>> digitToLetters;
        digitToLetters['2'] = {"a", "b", "c"};
        digitToLetters['3'] = {"d", "e", "f"};
        digitToLetters['4'] = {"g", "h", "i"};
        digitToLetters['5'] = {"j", "k", "l"};
        digitToLetters['6'] = {"m", "n", "o"};
        digitToLetters['7'] = {"p", "q", "r", "s"};
        digitToLetters['8'] = {"t", "u", "v"};
        digitToLetters['9'] = {"w", "x", "y", "z"};
    
        return combos(digits, digitToLetters);
    }
};
