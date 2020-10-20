# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        return self.bfs(root)
    
    def getSum(self, nodes):
        leavesSum = 0
        for node in nodes:
            leavesSum += node.val
        return leavesSum
    
    def bfs(self, root):
        currentLevel = [root]
        nextLevel = []
        
        while currentLevel:
            for node in currentLevel:
                if node.left != None:
                    nextLevel.append(node.left)
                if node.right != None:
                    nextLevel.append(node.right)
            if nextLevel == []:
                return self.getSum(currentLevel)
            currentLevel = nextLevel
            nextLevel = []
