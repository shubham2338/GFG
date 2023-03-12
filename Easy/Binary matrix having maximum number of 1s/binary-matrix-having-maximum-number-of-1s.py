#User function Template for python3

class Solution:
    def findMaxRow(self, mat, N):
        # Code here
        res=0
        ind=0
        for i in range(len(mat)):
            h=mat[i].count(1)
            if h>res:
                res=h
                ind=i
        return [ind,res]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        mat = []
        for i in range(n):
            A = [int(x) for x in input().split()]
            mat.append(A)
        ob=Solution()
        ans = []
        ans = ob.findMaxRow(mat, n)
        for i in range(2):
            print(ans[i], end =" ")
        print()
# } Driver Code Ends