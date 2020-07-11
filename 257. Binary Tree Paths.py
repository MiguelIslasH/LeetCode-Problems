# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.paths= []
        
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        self.dfs(root, "", True)
        
        return self.paths
    
    def dfs(self,root, path,first=False):
        if root == None:
            return
    
        if first:
            path += str(root.val)
        else:
            path += "->"+str(root.val)
        if self.isLeaftNode(root):
            self.paths.append(path)
            
        self.dfs(root.left, path)
        self.dfs(root.right, path)
        
    def isLeaftNode(self,node):
        if node.left == None and node.right==None:
            return True
        return False
