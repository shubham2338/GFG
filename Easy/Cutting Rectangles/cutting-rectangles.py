#User function Template for python3
import math
class Solution:
    def minimumSquares(self, L, B):
        # code here
        h=math.gcd(L,B)
        a=(L*B)//(h*h)
        return [a,h]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        L, B = [int(x) for x in input().split()]
        
        ob = Solution();
        N, K = ob.minimumSquares(L, B)
        print(N,end=" ")
        print(K)
# } Driver Code Ends