# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(root):
            if not root:
                return [0, True]
            left = getHeight(root.left)
            right = getHeight(root.right)
            if left[1] and right[1] and abs(left[0] - right[0]) <= 1:
                isBalanced = True
            else:
                isBalanced = False
            return [1 + max(left[0], right[0]), isBalanced]
        return getHeight(root)[1]