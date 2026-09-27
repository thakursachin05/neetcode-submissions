# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        mapX = defaultdict(int)
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            
            left_gain = max(dfs(node.left), 0)
            right_gain = max(dfs(node.right), 0)
            
            # Step 2: Calculate the value of the path turning at the current node
            current_path_sum = node.val + left_gain + right_gain
            
            # Step 3: Update our global maximum path sum found so far
            max_sum = max(max_sum, current_path_sum)
            
            # Step 4: For the parent call, we can only choose ONE branch (left or right)
            return node.val + max(left_gain, right_gain)
        dfs(root)
        return max_sum
        