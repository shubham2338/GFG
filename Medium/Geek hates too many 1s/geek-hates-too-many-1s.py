class Solution:
    def noConseBits(self, n : int) -> int:
        bs=bin(n)[2:]                           
        tl=[i for i in bs]                      
        i=0
        while i<len(bs)-1:
            if bs[i]=='1':
                c=1
                while c!=3:
                    i+=1
                    if i<len(bs) and bs[i]=='1':
                        c+=1
                    else:
                        i+=1
                        break
                else:
                    tl[i]='0'
                    i+=1
            else:
                i+=1
        bs=''.join(tl)                           
        return(int(bs,2))
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        obj = Solution()
        res = obj.noConseBits(n)
        
        print(res)
        

# } Driver Code Ends