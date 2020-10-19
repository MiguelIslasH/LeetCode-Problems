# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.minLevel = None
        self.dfs(root, 1)
        return self.minLevel
    
    def dfs(self, root, level):
        if root == None:
            return
        
        if root.left == None and root.right == None:
            if self.minLevel == None or level < self.minLevel  :
                self.minLevel = level
        
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)
            
