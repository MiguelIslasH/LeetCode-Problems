# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.trimedTree = None
        
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root == None:
            return
        
        if L <= root.val <= R:
            self.addNode(root.val, self.trimedTree)
        
        self.trimBST(root.left,L,R)
        self.trimBST(root.right,L,R)
        return self.trimedTree
            
    def addNode(self, value, root):
        if self.trimedTree == None:
            self.trimedTree = TreeNode(value)
            return
        
        if root == None:
            return
        
        if root.left == None or root.right == None:
            
            if value < root.val:
                if root.left == None:
                    root.left = TreeNode(value)
                else:
                    self.addNode(value, root.left)
            else:
                if root.right == None:
                    root.right = TreeNode(value)
                else:
                    self.addNode(value, root.right)
        else:
            if value < root.val:
                self.addNode(value, root.left)
            else:
                self.addNode(value, root.right)     
