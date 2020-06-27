# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.orderedNumbers=[]
        
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.fillList(root)
        newTree = TreeNode(self.orderedNumbers[0])
        currentNode = newTree
        
        for index in range(1, len(self.orderedNumbers)):
            currentNode.right = TreeNode(self.orderedNumbers[index])
            currentNode = currentNode.right
        
        return newTree
    
    def fillList(self, root):
        if root == None:
            return
        self.fillList(root.left)
        self.orderedNumbers.append(root.val)
        self.fillList(root.right)
        
