# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def heightOfTree(self, root):
        if root == None:
            return 0
        else:
            left = self.heightOfTree(root.left) + 1
            right = self.heightOfTree(root.right) + 1
            return max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        def solution(node):
            if node == None:
                return
            else:
                left = self.heightOfTree(node.left)
                right = self.heightOfTree(node.right)
                self.best = max(self.best, right + left)
                solution(node.left)
                solution(node.right)
        solution(root)
        return self.best            
        