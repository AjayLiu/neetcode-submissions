class Solution {
public:

    string encode(vector<string>& strs) {
        string encodedStr = "";
        for(string s : strs){
            int lenStr = s.size();
            encodedStr += to_string(lenStr) + "#" + s;
        }
        return encodedStr;
    }

    vector<string> decode(string s) {
        vector<string> decoded;
        size_t index = 0;
        size_t hashIndex = s.find("#");
        while(hashIndex != string::npos){
            string lenStr = s.substr(index, hashIndex - index);
            index = hashIndex;
            string thisStr = s.substr(index + 1, stoi(lenStr));
            index += stoi(lenStr) + 1;
            decoded.push_back(thisStr);

            hashIndex = s.find("#", index);
        }
        return decoded;
    }
};
