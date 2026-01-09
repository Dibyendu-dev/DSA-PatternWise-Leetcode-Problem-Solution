class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expectedSum = n*(n+1)//2
        actualSum = 0
        for i in nums:
           actualSum += i
        missingNums = ( expectedSum - actualSum)
        return missingNums
