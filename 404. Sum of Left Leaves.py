# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.leftLeaves = 0
        
    def sumOfLeftLeaves(self, root: TreeNode, left = None) -> int:
        if root == None:
            return 0
        
        if root.left == None and root.right == None and left:
            self.leftLeaves += root.val
        
        self.sumOfLeftLeaves(root.left, True)
        self.sumOfLeftLeaves(root.right)
        
        return self.leftLeaves
        
