def combinationSum(self, candidates, target):
        def func (candidates,index,target,ds,ans):
            if target == 0:
                ans.append(ds[:])
                return
            if index < 0 or target < 0:
                return
            
            # include
            ds.append(candidates[index])
            func(candidates,index,target-candidates[index],ds,ans)
            ds.pop()
            # exclude
            func(candidates,index-1,target,ds,ans)
           
        
        ans = []
        v = candidates[:]
        func(v, len(v) - 1, target, [], ans)
        return ans