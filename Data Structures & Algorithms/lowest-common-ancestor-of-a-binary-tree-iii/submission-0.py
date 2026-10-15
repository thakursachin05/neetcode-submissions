"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        visited = set()
        def dfs(node):
            if not node:
                return -1
            if node in visited:
                return node
            visited.add(node)
            return dfs(node.parent)
       
        
        dfs(p)

        return dfs(q)