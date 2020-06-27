# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1==None and t2==None:
            return None
        
        if t1!=None and t2!=None:
            root = TreeNode(t1.val+t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)

        elif t1 == None:
            root = TreeNode(0+t2.val)
            root.left = self.mergeTrees(None, t2.left)
            root.right = self.mergeTrees(None, t2.right)
        else:
            root = TreeNode(t1.val+0)
            root.left = self.mergeTrees(t1.left, None)
            root.right = self.mergeTrees(t1.right, None)
        
        return root
