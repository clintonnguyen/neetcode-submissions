# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        current = root
        if current:
            current.left, current.right = current.right, current.left
        else:
            return None
        self.invertTree(current.left)
        self.invertTree(current.right)
        return current