class Solution {

    int lowerBound(vector<int>& nums, int target) {
        int lo = 0;
        int hi = nums.size()-1;
        int ans = nums.size();
        while(lo<=hi){
            int mid = lo + (hi -lo)/2;
            if(nums[mid]< target){
                lo = mid+1;
            }else{
                ans = mid;
                hi = mid -1;
            }
        }
        return ans;
    }

    int upperBound(vector<int>& nums, int target) {
        int lo = 0;
        int hi = nums.size()-1;
        int ans = nums.size();
        while(lo<=hi){
            int mid = lo + (hi -lo)/2;
            if(nums[mid]<= target){
                lo = mid+1;
            }else{
                ans = mid;
                hi = mid -1;
            }
        }
        return ans;
    }

public:
    vector<int> searchRange(vector<int>& nums, int target) {
        int lb = lowerBound(nums,  target);
        if(lb == nums.size() || nums[lb] != target){
            return {-1,-1};
        }
        int ub = upperBound( nums, target);
        return {lb, ub-1};
    }
     
};