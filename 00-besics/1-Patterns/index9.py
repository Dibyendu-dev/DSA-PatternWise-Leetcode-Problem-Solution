class Solution:
    def pattern9(self, n):
        self.pyramid(n)
        self.inverted_pyramid(n)
    def pyramid(self, n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ", end="")
            for j in range(2*i+1):
                print("*",end="")
            print()
    def inverted_pyramid(self, n):
        for i in range(n):
            for j in range(i):
                print(" ",end="")
            for j in range(2*n-(2*i+1)):
                print("*", end="")
            print()