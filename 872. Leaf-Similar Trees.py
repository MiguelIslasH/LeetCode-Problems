# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
            self.sequence = []
            self.are_leaf_similar = True
            self.index = 0
            
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        self.dfs(root1,1)
        self.dfs(root2,2)
        return self.are_leaf_similar
        
    def dfs(self, root, whichTree):
        if root == None:
            return
        
        if root.left == None and root.right == None:
            if whichTree == 1: 
                self.sequence.append(root.val)
            else:
                if root.val != self.sequence[self.index]:
                    self.are_leaf_similar = False
                self.index +=1
            return
        
        if self.are_leaf_similar == False:
            return
        
        self.dfs(root.left,whichTree)
        self.dfs(root.right, whichTree)
        
        
