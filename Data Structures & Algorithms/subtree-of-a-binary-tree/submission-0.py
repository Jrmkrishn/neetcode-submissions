# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def dfs(self, node1, node2):
        if not node1 and not node2:
            return True
        if not node1 or not node2 or node1.val != node2.val:
            return False
        return self.dfs(node1.left, node2.left) and self.dfs(node1.right, node2.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        node1 = root
        node2 = subRoot
        queue = deque([node1])
        while queue:
            node1 = queue.popleft()
            if node1.val == node2.val and self.dfs(node1, node2):
                return True  
            if node1.left:
                queue.append(node1.left)
            if node1.right:
                queue.append(node1.right)
        
        return False