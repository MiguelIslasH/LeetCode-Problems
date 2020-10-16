# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        self.depth = 0
        self.findTreeDepth(root, 0)
        self.mostRightNodes=[None for _ in range(self.depth+1)]
        self.dfs(root, 0)
        
        return self.mostRightNodes
        
    def findTreeDepth(self, root, level):
        if root==None:
            return
        
        if(level>self.depth):
            self.depth = level
            
        self.findTreeDepth(root.left, level+1)
        self.findTreeDepth(root.right, level+1)
        
        
    def dfs(self, root, level):
        if root == None:
            return
        
        if self.mostRightNodes[level] == None:
            self.mostRightNodes[level] = root.val
        
        self.dfs(root.right, level+1)
        self.dfs(root.left, level+1)
