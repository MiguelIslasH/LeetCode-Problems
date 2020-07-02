# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.complementNumbers = set()
        self.existSum = False
        
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if root == None:
            return
        
        if root.val in self.complementNumbers:
            self.existSum = True
        
        self.complementNumbers.add(k-root.val)
        self.findTarget(root.left, k)
        self.findTarget(root.right, k)
        
        return self.existSum
