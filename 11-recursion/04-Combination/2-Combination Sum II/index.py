def combinationSum2(self, candidates, target):
        def func (index,target,ds,candidates):
            if target == 0:
                ans.append(ds[:])
                return
            if index >= len(candidates) or target < 0:
                return
            
            # include
            ds.append(candidates[index])
            func(index+1,target-candidates[index],ds,candidates)
            ds.pop()
            # exclude
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            func(index+1,target,ds,candidates)
           
        candidates.sort()
        ans = []
        func(0, target, [], candidates)
        return ans