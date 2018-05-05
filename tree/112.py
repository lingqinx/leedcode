# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
#it cannot get the right answer        
        if not root:
            return False
        add=0
        
        if root.left == None and root.right == None and root.val == sum:          
            if add == sum:
                return True  
                
        if root.right!=None:
            self.hasPathSum(root.right,sum)
        if root.left!=None:
            self.hasPathSum(root.left,sum)

        return False
        """
        if not root:
            return False
        
        if root.left == None and root.right == None and root.val == sum:          
            return True  
                
        sum= sum-root.val

        return self.hasPathSum(root.right,sum) or self.hasPathSum(root.left,sum)

            
            
        