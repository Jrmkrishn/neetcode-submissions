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

        tmp1, tmp2 = node.left, node.right
        node.left = tmp2
        node.right = tmp1
        self.change_children(node.left)
        self.change_children(node.right)
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        cur = root
        self.change_children(cur)
        return root