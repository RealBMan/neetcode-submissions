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

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        if root == None:
            return True
        else:
            def calculate(node):
                if node == None:
                    return None
                else:
                    left = self.heightOfTree(node.left)
                    right = self.heightOfTree(node.right)
                    if abs(left - right) > 1:
                        self.isBalanced = False 
                    calculate(node.left)
                    calculate(node.right)
            calculate(root)
            return self.isBalanced
        

        