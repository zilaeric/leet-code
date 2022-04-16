# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    total = 0
    
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None: 
            return None
        
        if root.right != None:
            root.right = self.convertBST(root.right)
        
        self.total += root.val
        root.val = self.total
        
        if root.left != None:
            root.left = self.convertBST(root.left)
            
        return root

