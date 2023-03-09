#User function Template for python3

from typing import List
class Solution:
    class Node:
        def __init__(self, data=None):
            self.data = data
            self.next = None
    def isAnagram(self, cnts, cntl):
        for i in range(26):
            if cnts[i] == cntl[i]:
                continue
            else:
                return False
        return True
    def findAnagrams(self, head: Node, s: str) -> List[Node]:
        cnts = [0] * 26
        sz = len(s)
        for it in s:
            cnts[ord(it) - ord('a')] += 1
        cntl = [0] * 26
        i = head
        j = head
        ans = []
        szL = 0
        while j is not None:
            cntl[ord(j.data) - ord('a')] += 1
            szL += 1
            if szL == sz:
                ok = self.isAnagram(cnts, cntl)
                if ok:
                    tmp = j.next
                    j.next = None
                    ans.append(i)
                    cntl = [0] * 26
                    j = tmp
                    i = j
                    szL = 0
                else:
                    cntl[ord(i.data) - ord('a')] -= 1
                    i = i.next
                    j = j.next
                    szL -= 1
            else:
                j = j.next
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class
class Node:
    def __init__(self):
        self.data = None
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
    def insert(self, data):
        if self.head == None:
            self.head = Node()
            self.tail = self.head
            self.head.data = data
        else:
            new_node = Node()
            new_node.data = data
            new_node.next = None
            self.tail.next = new_node
            self.tail = self.tail.next
            
def printlist(head):
    temp = head
    while temp is not None:
        print(temp.data, end=" ")
        temp = temp.next
    print('')

# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        list1 = Linked_List()
        n = int(input())
        values = list(map(str, input().strip().split()))
        for i in values:
            list1.insert(i)
        s = input()
        res = Solution().findAnagrams(list1.head, s)
        for i in range(len(res)):
            printlist(res[i])
        if len(res) == 0:
            print(-1)
            
# } Driver Code Ends