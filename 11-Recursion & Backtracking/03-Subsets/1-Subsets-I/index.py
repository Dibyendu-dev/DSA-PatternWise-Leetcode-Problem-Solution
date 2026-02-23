class Solution:
    def subsetSums(self, nums):
        def func (index,sum,nums,ans):
            if index == len(nums):
                ans.append(sum)
                return
            
            # include
            func(index+1,sum+nums[index],nums,ans)
            # exclude
            func(index+1,sum,nums,ans)
        ans = []
        func(0,0,nums,ans)  
        return ans