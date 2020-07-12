# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ancestorOfP = set()
        self.LCA = None
        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.fillAncestors(root,p)
        self.checkAncestors(root,q, None)
        
        return TreeNode(self.LCA)
    
    def fillAncestors(self, root, p):
        if root.val < p.val:
            self.ancestorOfP.add(root.val)
            self.fillAncestors(root.right, p)
        elif root.val > p.val:
            self.ancestorOfP.add(root.val)
            self.fillAncestors(root.left, p)
        elif root.val == p.val:
            self.ancestorOfP.add(root.val)
        
    def checkAncestors(self, root, q, lastNode):
        
        if root.val < q.val:
            if root.val in self.ancestorOfP:
                lastNode = root.val
                self.checkAncestors(root.right, q, lastNode)
            else:
                self.LCA = lastNode
        elif root.val > q.val:
            if root.val in self.ancestorOfP:
                lastNode = root.val
                self.checkAncestors(root.left, q, lastNode)
            else:
                self.LCA = lastNode
        elif root.val == q.val:
            if lastNode == None:
                lastNode = root.val
            if root.val in self.ancestorOfP:
                lastNode = root.val
            self.LCA = lastNode
            
