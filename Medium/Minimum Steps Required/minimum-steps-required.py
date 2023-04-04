class Solution:
    def minSteps(self, str : str) -> int:
        st=str
        prev='#'
        ac=0
        bc=0
        for i in st:
            if i==prev:continue
            if i=='a':ac+=1
            if i=='b':bc+=1
            prev=i
        return min(ac,bc)+1
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        str = (input())
        
        obj = Solution()
        res = obj.minSteps(str)
        
        print(res)
        

# } Driver Code Ends