# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.isBST = True
        self.lastNumber = None
    def isValidBST(self, root: TreeNode) -> bool:
        self.dfs(root)
        return self.isBST
    
    def dfs(self, root):
        if root == None:
            return
        if self.isBST == False:
            return
        
        self.dfs(root.left)
        if self.lastNumber == None:
            self.lastNumber = root.val
        elif self.lastNumber>=root.val:
            self.isBST = False
        else:
            self.lastNumber = root.val
        self.dfs(root.right)
