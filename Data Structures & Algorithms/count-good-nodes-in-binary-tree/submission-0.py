# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def dfs(self, node, max_val, result):
        if not node:
            return
        if node.val >= max_val:
            print("node ", node.val)
            result.append(node.val)
            max_val = node.val
        if node.left:
            self.dfs(node.left, max_val, result)
        if node.right:
            self.dfs(node.right, max_val, result)
    
    def goodNodes(self, root: TreeNode) -> int:
        result = []
        max_val = root.val
        cur = root
        self.dfs(root, max_val, result)
        return len(result)