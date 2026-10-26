# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def ancestors(self,root, ans):
        if root is None:
            return ans
        else:
            ans.append(root)
            ans.extend(self.ancestors(root.left, ans))
            ans.extend(self.ancestors(root.right, ans))
            return ans
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root is None or p is None or q is None:
            return None
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
            
        
        