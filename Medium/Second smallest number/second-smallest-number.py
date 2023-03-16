#User function Template for python3

class Solution:
    def secondSmallest(self, S, D):
        st=""
        if(D*9<=S):
            return -1
        for i in range(D,0,-1):
            if(S==1):
                if(i==1):
                    st+="1"
                else:
                    st+="0"
            elif S-1>=9:
                st+="9"
                S-=9
            else:
                if(i==1):
                    st+=str(S)
                else:
                    st+=str(S-1)
                    S-=S-1
        x=""
        for i in range(D):
            if(st[i+1]!='9'):
                x+=str(int(st[i])-1)
                x+=str(int(st[i+1])+1)
                x+=st[i+2:]
                break
            x+=st[i]
        return int(x[::-1])


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S,D=map(int,input().strip().split(" "))

        ob = Solution()
        print(ob.secondSmallest(S,D))
# } Driver Code Ends