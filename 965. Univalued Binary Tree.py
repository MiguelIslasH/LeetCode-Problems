class Solution:
    def __init__(self):
        self.isUnivaluaded = True
        self.uniqueValue = None
        
    def isUnivalTree(self, root: TreeNode) -> bool:
        self.uniqueValue = root.val
        self.dfs(root)
        return self.isUnivaluaded
    
    def dfs(self, root: TreeNode):
        if not self.isUnivaluaded:
            return
        if root == None:
            return
        if root.val != self.uniqueValue:
            self.isUnivaluaded = False
        
        self.dfs(root.left)
        self.dfs(root.right)
