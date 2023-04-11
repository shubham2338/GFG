#User function Template for python3

class Solution():
    def solve(self, a, b, c):
        #your code goes here
        h=[a,b,c]
        h.sort()
        f=sum(h)
        if h[-1]<=2*(f-h[-1]+1):
            return sum(h)
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

from collections import Counter
for _ in range(int(input())):
    a, b, c=map(int,input().split())
    obj = Solution()
    res = obj.solve(a, b, c)
    
    print(res)
# } Driver Code Ends