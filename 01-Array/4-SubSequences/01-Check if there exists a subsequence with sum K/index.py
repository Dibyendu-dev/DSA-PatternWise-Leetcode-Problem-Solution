class Solution:
    def solve(self, i, n, arr, k,memo):
        if k == 0:
            return True
        if k < 0 or i >= n:
            return False
        if (i, k) in memo:
                return memo[(i, k)]
        
        include = self.solve(i+1, n, arr, k-arr[i],memo)
        exclude = self.solve(i+1, n, arr, k,memo)

        result = include or exclude
        memo[(i, k)] = result
        return result         

    def checkSubsequenceSum(self, nums, k):
        n = len(nums)
        memo = {}
        return self.solve(0,n,nums,k,memo)
        
