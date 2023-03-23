#User function Template for python3

'''
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
'''

class Solution:
    def maxDifferenceBST(self,root, target):
        #code here
        def fun1(root):
            if root is None:
                return 1e9
            if root.left is None and root.right is None:
                return root.data
            l=fun1(root.left)
            r=fun1(root.right)
            return min(l,r)+root.data
        ans=[0]
        def fun(root,t):
            if root is None:
                return -1
            if root.data==t:
                ans[0]=min(fun1(root.left),fun1(root.right))
                return 0
            if root.data>t:
                h=fun(root.left,t)
            else:
                h=fun(root.right,t)
            if h!=-1:
                return h+root.data
            else:
                return -1
            
        res=fun(root,target)
        if ans[0]==1e9:
            return res
        return res-ans[0]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    def createNode(self, data):
        return Node(data)
    
    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        else:
            if data < node.data:
                node.left = self.insert(node.left, data)
            else:
                node.right = self.insert(node.right, data)
            return node

    def traverseInorder(self, root):
        if root is not None:
            print(root.data, end= " ")
            self.traverseInorder(root.left)
            self.traverseInorder(root.right)
    
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        arr = input().strip().split()
        root = None
        tree = Tree()
        root = tree.insert(root, int(arr[0]))
        for j in range(1, n):
            root = tree.insert(root, int(arr[j]))
        #tree.traverseInorder(root)
        target = int(input())
        
        res = Solution().maxDifferenceBST(root, target)
        print(res)

# } Driver Code Ends