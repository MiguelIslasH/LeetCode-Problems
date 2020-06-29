"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.numbers = []
    def postorder(self, root: 'Node') -> List[int]:
        self.postorderList(root)
        return self.numbers
    
    def postorderList(self, root: 'Node'):
        if root == None:
            return
        
        for node in root.children:
            self.postorder(node)
        self.numbers.append(root.val)
        
