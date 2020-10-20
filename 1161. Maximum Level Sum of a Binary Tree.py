# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        self.maxSum = [root.val, 1]
        self.bfs(root)
        return self.maxSum[1]
        
    def checkSumLevel(self, nodes, level):
        sumOfNodes = 0
        if nodes == []:
            return
        for node in nodes:
            sumOfNodes += node.val
        
        if sumOfNodes > self.maxSum[0]:
            self.maxSum[0] = sumOfNodes
            self.maxSum[1] = level
        
    def bfs(self, root):
        currentLevel = [root]
        nextLevel = []
        level = 1
        while currentLevel:
            level+=1
            for node in currentLevel:
                if node.left!=None:
                    nextLevel.append(node.left)
                if node.right!=None:
                    nextLevel.append(node.right)
            self.checkSumLevel(nextLevel, level)
            currentLevel = nextLevel
            nextLevel = []
        
        
