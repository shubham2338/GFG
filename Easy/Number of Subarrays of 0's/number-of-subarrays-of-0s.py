#User function Template for python3

class Solution():
    def no_of_subarrays(self, n,arr):
        #your code goes here
        res=0
        c=0
        for i in arr:
            if i==0:
                c+=1
                res+=c
            else:
                c=0
            
        return res
            
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    print(Solution().no_of_subarrays(n, arr))
# } Driver Code Ends