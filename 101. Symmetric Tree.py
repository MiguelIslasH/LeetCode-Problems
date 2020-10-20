class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        
        return self.bfs(root)
    
    def checkSymmetric(self, nodes):
        for iterator in range(0, len(nodes)//2):
            if nodes[iterator] == None and nodes[len(nodes)-1-iterator]!=None:
                return False
            if nodes[iterator] != None and nodes[len(nodes)-1-iterator]==None:
                return False
            if nodes[iterator] == None and nodes[len(nodes)-1-iterator]==None:
                continue
            if nodes[iterator].val != nodes[len(nodes)-1-iterator].val:
                return False
        return True
        
    def bfs(self, root):
        currentLevel = [root]
        nextLevel = []
        
        while currentLevel:
            for node in currentLevel:
                if node == None:
                    continue

                nextLevel.append(node.left)
                nextLevel.append(node.right)
            if self.checkSymmetric(nextLevel) == False:
                return False
            
            currentLevel = nextLevel
            nextLevel = []
        return True
    
