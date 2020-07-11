# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.sumOfLevels = {}
        self.nodesPerLevel = {}
        
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root == None:
            return 0
        
        self.dfs(root,0)
        avaragePerLevel = [] 
        for index,key in enumerate(self.sumOfLevels):
            avaragePerLevel.append(self.sumOfLevels[key]/self.nodesPerLevel[key])
        
        return avaragePerLevel
    
    def dfs(self, root, level):
        if root == None:
            return 0
        
        if level not in self.sumOfLevels:
            self.sumOfLevels[level] = root.val
        else:
            self.sumOfLevels[level] += root.val
        
        if level not in self.nodesPerLevel:
            self.nodesPerLevel[level] = 1
        else:
            self.nodesPerLevel[level] += 1
        
        self.dfs(root.left, level+1)
        self.dfs(root.right, level+1)
        
