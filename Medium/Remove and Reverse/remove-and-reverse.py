#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def removeReverse(self, S): 
        d={}
        for i in S:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        i=0
        fl=0
        j=len(S)-1
        cnt=0
        while i<len(S) and j>=0:
            if fl==0 and d[S[i]]>=2:
                d[S[i]]-=1
                S=S[:i]+S[i+1:]
                fl=1
                i+=1
                j=len(S)-1
                cnt+=1
            else:
                i+=1
            if fl==1 and d[S[j]]>=2:
                cnt+=1
                d[S[j]]-=1
                S=S[:j]+S[j+1:]
                fl=0
                j-=1
                i=0
            else:
                j-=1
        if cnt%2==0:
            return S
        return S[::-1]
            
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.removeReverse(S)
        print(ans)


# } Driver Code Ends