class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();
        
        // PHASE 1: Clean up the array
        // Replace all invalid numbers with a placeholder (we'll use n+1)
        for(int i = 0; i < n; i++) {
            if(nums[i] <= 0 || nums[i] > n) {
                nums[i] = n + 1;  // Out of range, won't affect our answer
            }
        }
        
        // PHASE 2: Mark presence by making indices negative
        // If number k exists, make nums[k-1] negative
        for(int i = 0; i < n; i++) {
            int val = abs(nums[i]);  // Get actual value (might be negative from marking)
            
            if(val <= n) {  // Only mark if in valid range
                nums[val - 1] = -abs(nums[val - 1]);  // Mark as negative
            }
        }
        
        // PHASE 3: Find first positive index
        // First positive index i means number (i+1) is missing
        for(int i = 0; i < n; i++) {
            if(nums[i] > 0) {
                return i + 1;
            }
        }
        
        // All numbers 1 to n are present
        return n + 1;
    }
};
