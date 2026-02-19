def subsetsWithDup(self, nums):
        def func (index,ds,nums,ans):
            if index == len(nums): #base case
                ans.append(ds[:])
                return
           # include
            ds.append(nums[index])
            func(index+1,ds,nums,ans)
            ds.pop()
            # exclude
            for j in range(index+1,len(nums)):
                if nums[j] != nums[index]:
                    func(j,ds,nums,ans)
                    return
            func(len(nums),ds,nums,ans)
        
        ans = []
        arr = []
        nums.sort()
        func(0,arr,nums,ans)  
        return ans