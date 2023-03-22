#User function Template for python3

class Solution:
    def solve (self, X, Y, S):
        def fun(x,y,s,st):
            stack=[]
            i=0
            ans=0
            while i<len(s):
                if stack and stack[-1]==st[0] and s[i]==st[1]:
                    ans+=x
                    stack.pop(-1)
                else:
                    stack.append(s[i])
                i+=1
            s=''
            while stack:
                s+=stack.pop(-1)
            i=0
            while i<len(s):
                if stack and stack[-1]==st[0] and s[i]==st[1]:
                    ans+=y
                    stack.pop(-1)
                else:
                    stack.append(s[i])
                i+=1
            return ans
            
        if X>Y:
            h=fun(X,Y,S,'pr')
        else:
            h=fun(Y,X,S,'rp')
        return h
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str = input().split()
        X = int(str[0])
        Y = int(str[1])
        S = input()
        

        ob = Solution()
        print(ob.solve(X,Y,S))
# } Driver Code Ends