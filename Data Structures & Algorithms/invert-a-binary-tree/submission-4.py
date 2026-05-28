# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def change_children(self, node):
        if not node:
            return None

        node.right, node.left = node.left, node.right
        
        self.change_children(node.left)
        self.change_children(node.right)
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.change_children(root)
        return root