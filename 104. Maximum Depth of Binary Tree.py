class Solution:
    def __init__(self):
            self.maximumDepth = 0
            
    def maxDepth(self, root: TreeNode) -> int:
        self.dfs(root, 1)
        return self.maximumDepth
    
    def dfs(self, root: TreeNode, currentLevel):
        if root == None:
            return
        
        if root.left == None and root.right == None:
            if currentLevel > self.maximumDepth:
                self.maximumDepth = currentLevel
            return 
        
        self.dfs(root.left, currentLevel + 1)
        self.dfs(root.right, currentLevel + 1)
