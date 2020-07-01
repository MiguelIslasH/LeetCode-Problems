"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.preorderList = []
        
    def preorder(self, root: 'Node') -> List[int]:
        if root==None:
            return
        
        self.preorderList.append(root.val)
        for kid in root.children:
            self.preorder(kid)
        return self.preorderList
            
