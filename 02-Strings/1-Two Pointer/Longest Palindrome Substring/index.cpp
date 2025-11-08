class Solution {
public:
    string longestPalindrome(string s) {
        if (s.length()<2) return s;
        int start =0;
        int maxLength = 1;
        for(int i=0;i<s.length();i++){
            int oddLength = expandArroundCenter(s,i,i);
            int evenLength = expandArroundCenter(s,i,i+1);
            int len = max(oddLength, evenLength);
            if(len > maxLength){
                maxLength = len;
                start = i-(len-1)/2;
            }
        }
        return s.substr(start,maxLength);
    }

 private:
    int expandArroundCenter(string &s, int left, int right){
        while(left>=0 && right<s.length() && s[left]==s[right]){
            left--;
            right++;
        }
        return right-left-1;
    }

};