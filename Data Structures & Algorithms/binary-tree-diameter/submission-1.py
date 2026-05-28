# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root):
        res = 0
        def dfs(cur):
            if not cur:
                return 0
            nonlocal res
            left = dfs(cur.left)
            right = dfs(cur.right)

            diameter = left + right
            res = max(left+right, res)
            return 1 + max(left, right)
        dfs(root)
        return res 