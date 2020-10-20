# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        return self.bfs(root)
        
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
                return currentLevel[0].val
            currentLevel = nextLevel
            nextLevel = []
