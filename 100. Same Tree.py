# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sameTree = True
        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        
        elif p == None and q != None:
            self.sameTree = False
            return
        
        elif q == None and p != None:
            self.sameTree = False
            return
        
        if p.val != q.val:
            self.sameTree = False
            return
        
        self.isSameTree(p.left, q.left)
        self.isSameTree(p.right, q.right)
        
        return self.sameTree
