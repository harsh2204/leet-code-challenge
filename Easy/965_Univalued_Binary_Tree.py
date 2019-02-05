# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: 'TreeNode') -> 'bool':
        if root == None:
            return True
        if root.left and root.right:
            if(root.val != root.right.val or root.val != root.left.val):
                return False
        elif root.left:
            if(root.val != root.left.val):
                return False
        elif root.right:
            if(root.val != root.right.val):
                return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
        return True
        
