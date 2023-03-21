#Initial Template for Python 3
class Solution:
	def ZigZagMaxLength(self, nums):
		# Code here
		l,r=1,1
		for i in range(1,len(nums)):
		    if nums[i]>nums[i-1]:
		        l=r+1
		    elif nums[i]<nums[i-1]:
		        r=l+1
		return max(l,r)
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.ZigZagMaxLength(A))
# } Driver Code Ends