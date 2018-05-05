# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #find one path
    def findpath(self,root,target):
        if root:
            return int(root.val == target)+self.findpath(root.right,target-root.val)+self.findpath(root.left,target-root.val)
        return 0
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root:
            return self.findpath(root,sum)+self.pathSum(root.left,sum)+self.pathSum(root.right,sum)
        return 0
        
            
            
        