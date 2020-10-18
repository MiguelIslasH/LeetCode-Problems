# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.inOrder = []
        self.dfs(root)
        return self.inOrder
    
    def dfs(self, root):
        if root == None:
            return
        
        self.dfs(root.left)
        self.inOrder.append(root.val)
        self.dfs(root.right)
