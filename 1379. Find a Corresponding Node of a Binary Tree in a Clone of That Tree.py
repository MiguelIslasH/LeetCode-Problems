# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.reference = None
        self.dfs(cloned, target)
        return self.reference
    
    def dfs(self, root, target):
        if root == None and target == None:
            return None
    
        if root == None:
            return
        
        if root.val == target.val:
            self.reference = root
            return
    
        self.dfs(root.left, target)
        self.dfs(root.right, target)
        
