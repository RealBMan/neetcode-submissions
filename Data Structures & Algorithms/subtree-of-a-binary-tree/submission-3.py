# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None: 
            return True
        if p is None or q is None: 
            return False
        elif p.val != q.val:
            return False
        else:
            if p.val != q.val:
                return False
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)
            return left and right

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root == None:
            return False
        if self.isSameTree(root, subRoot):
            return True
        else:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            return left or right
        