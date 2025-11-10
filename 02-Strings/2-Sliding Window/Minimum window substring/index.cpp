class Solution {
public:
    string minWindow(string s, string t) {
        if(s.empty() || t.empty()) return "";

        vector<int> need(128, 0);
        for(char c : t){
            need[c]++;
        }

        int required = t.size();

        int left =0;
        int right =0;
        int minLength = INT_MAX;
        int minStart=0;

        while(right< s.size()){
            char currentChar = s[right];

            if(need[currentChar] > 0){
                required--;
            }

            need[currentChar]--;

            while (required == 0){
                int currentLength = right - left + 1;
                if (currentLength < minLength) {
                    minLength = currentLength;
                    minStart = left;
                }

                char leftChar = s[left];
                 need[leftChar]++;

                if(need[leftChar] > 0) {
                    required++;
                }
                left++;
            }
            right++;
        }
        if (minLength == INT_MAX) {
            return "";  
        }
        
        return s.substr(minStart, minLength);
    }
};