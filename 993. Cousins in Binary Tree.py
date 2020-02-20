# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
            self.xHeight = 0
            self.yHeight = 0
            self.haveSameParent = False
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        self.dfs(root, x, y, -1)
        if self.xHeight==self.yHeight:
            return True
        else:
            return False
        
    def dfs(self, root, x , y, level):
        if root == None:
            return
        if self.haveSameParent:
            return
        
        if root.left!=None and root.right!=None:
            if root.left.val == x and root.right.val == y:
                self.haveSameParent = True
                self.xHeight=-1
                self.yHeight=-2
                return 
            
            if root.left.val == y and root.right.val == x:
                self.xHeight=-1
                self.yHeight=-2
                self.haveSameParent = True
                return
        
        level +=1
        
        if root.val == x:
            self.xHeight = level
        
        if root.val == y :
            self.yHeight = level
        
        self.dfs(root.left, x , y, level)
        self.dfs(root.right, x , y, level)
        
