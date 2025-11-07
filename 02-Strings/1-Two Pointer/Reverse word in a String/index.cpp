class Solution {
public:
    string reverseWords(string s) {
        string result ="";
        int n= s.length();
        int i= n-1;
        while(i>=0){
            while(i>=0 && s[i]== ' ') i--;
            if(i< 0) break;
            int j = i;
            while(j >=0 && s[j] != ' ') {
                j--;
            }
            string word = s.substr(j+1, i-j);
            if(result.empty()) {
                result = word;
            }
            else {
                result += " " + word;
            }
            i=j;
        }
        return result;
    }
};