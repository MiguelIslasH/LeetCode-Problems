# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.nodesLevel= {}
    
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        self.transversal(root, 0)
        valueOfNodes = []
        
        for key in reversed(self.nodesLevel):
            valueOfNodes.append(self.nodesLevel[key])
        
        return valueOfNodes
            
    def transversal(self, root, level):
        if root == None:
            return 0
    
        if self.nodesLevel.get(level) == None:
            self.nodesLevel[level] = [root.val]
        else:
            self.nodesLevel[level].append(root.val)
        
        self.transversal(root.left, level+1)
        self.transversal(root.right, level+1)
