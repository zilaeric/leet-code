# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if low <= root.val <= high:
            if root.left != None:
                root.left = self.trimBST(root.left, low, high)
            if root.right != None:
                root.right = self.trimBST(root.right, low, high)
        elif root.val < low:
            if root.right != None:
                return self.trimBST(root.right, low, high)
            else:
                return None
        else:
            if root.left != None:
                return self.trimBST(root.left, low, high)
            else:
                return None

        return root
        
