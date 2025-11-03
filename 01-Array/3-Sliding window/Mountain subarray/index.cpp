class Solution {
public:
    int longestMountain(vector<int>& arr) {
        int n = arr.size();
        if(n<3) return 0;
        int longest = 0;
        for(int i=1;i<n-1;i++){
            if(arr[i]> arr[i-1] && arr[i]>arr[i+1]){
                int left =i;
                int right =i;
                while(left>0 && arr[left-1]< arr[left]){
                    left --;
                }
                while(right<n-1 && arr[right]>arr[right+1]){
                    right++;
                }
                int length = (right-left+1);
                longest = max(longest,length);
                i=right;
            }
        }
        return longest;
    }
};