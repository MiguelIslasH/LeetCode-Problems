# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        self.sumOfNumbers = 0
        self.dfs(root)
        return self.sumOfNumbers
        
    def sumGrandSons(self, root):
        if root.left != None:
            if root.left.left != None:
                self.sumOfNumbers += root.left.left.val
            if root.left.right != None:
                self.sumOfNumbers += root.left.right.val
        
        if root.right != None:
            if root.right.left != None:
                self.sumOfNumbers += root.right.left.val
            if root.right.right != None:
                self.sumOfNumbers += root.right.right.val
        
    def dfs(self, root):
        if root == None:
            return
    
        if root.val % 2 == 0:
            self.sumGrandSons(root)
            
        self.dfs(root.left)
        self.dfs(root.right)
