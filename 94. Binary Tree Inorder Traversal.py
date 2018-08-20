# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    #result=[] 如果设为全局变量，每次调用函数之前的也存在
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        #list的+与string同
        return self.inorderTraversal(root.left) + [root.val]+self.inorderTraversal(root.right)
        """
        if root.left!=None:
            self.inorderTraversal(root.left)
        self.result.append(root.val)
        if root.right!=None:
            self.inorderTraversal(root.right)
        return self.result
        """
