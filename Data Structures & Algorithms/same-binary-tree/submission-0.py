# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, cur1, cur2):
        if not cur1 and not cur2:
            return True
        if not cur1 or not cur2 or cur1.val != cur2.val:
            return False
        left = self.dfs(cur1.left, cur2.left)
        right = self.dfs(cur1.right, cur2.right)
        return left and right

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        cur1 = p
        cur2 = q
        res = self.dfs(p, q)
        return res