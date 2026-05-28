# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bfs(self, cur, level, result):
        if not cur:
            return 
        result[level].append(cur.val)
        if cur.left:
            self.bfs(cur.left, level+1, result)
        if cur.right:
            self.bfs(cur.right, level+1, result)
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        cur = root
        level = 1
        result = defaultdict(list)
        self.bfs(cur, level, result)
        return [val for val in result.values()]