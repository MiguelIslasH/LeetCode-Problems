# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root == None:
            return -1
        self.minimum = float("inf")
        self.second = float("inf")
        self.dfs(root, True)
        self.dfs(root, False)
        
        if self.second == float("inf"):
            return -1
        return self.second
    
    def dfs(self, root, first):
        if root == None:
            return
    
        if first:
            if root.val < self.minimum:
                self.minimum = root.val
        else:
            if root.val < self.second and root.val != self.minimum:
                self.second = root.val
        
        self.dfs(root.left, first)
        self.dfs(root.right, first)
