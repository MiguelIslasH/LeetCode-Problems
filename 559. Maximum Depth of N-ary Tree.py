"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def __init__(self):
        self.maxDepthTree = 0
        
    def maxDepth(self, root: 'Node', depth=1)-> int:
        if root == None:
            return 0
        
        if root.children==[]:
            if depth > self.maxDepthTree:
                self.maxDepthTree = depth
        
        
        for kid in root.children:
            self.maxDepth(kid, depth+1)
        
        return self.maxDepthTree
        
