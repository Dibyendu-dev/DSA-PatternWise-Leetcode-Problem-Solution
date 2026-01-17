class Solution:
    def countSubstrings(self, s: str) -> int:
        count =0
        n=len(s)
        for i in range(n):
            count +=self.countPalindrome(s,i,i)
            count +=self.countPalindrome(s,i,i+1)
        return count
    
    def countPalindrome(self, s: str, left: int, right: int) -> int:
        count = 0
        while left >=0 and right < len(s) and s[left] == s[right]:
            count +=1
            left -=1
            right +=1
        return count