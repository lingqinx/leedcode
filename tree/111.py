import Queue  
  
class Node:  
    def __init__(self,value=None,left=None,right=None):  
        self.value=value  
        self.left=left  
        self.right=right  

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.right and root.left:         
            return 1+min(self.minDepth(root.left),self.minDepth(root.right))
        if not root.left:#root.left==None add right
            return 1+self.minDepth(root.right)
        if not root.right:
            return 1+self.minDepth(root.left)
        else:
            return 1  
  
if __name__=='__main__':  
    so = Solution()
    root=Node('D',Node('B',Node('A'),Node('C')),Node('E',right=Node('G',Node('F'))))   
    print so.minDepth(root) 
