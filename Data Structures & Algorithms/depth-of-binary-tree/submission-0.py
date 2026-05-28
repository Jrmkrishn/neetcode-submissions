# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def find_depth(self, node, depth):
        if not node:
            return depth
        print(node.val, depth)
        depth += 1
        depthLeft = self.find_depth(node.left, depth)
        depthRight = self.find_depth(node.right, depth)
        
        depth = max(depthLeft, depthRight) 
        return depth
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = self.find_depth(root, 0)
        return count

