class Solution:
    def __init__(self):
        self.sumOfBinaryNumbers = 0
        
    def sumRootToLeaf(self, root: TreeNode) -> int:
        self.dfs(root, "")
        return self.sumOfBinaryNumbers
        
    def dfs(self, root, binaryNumber): 
        if root == None:
            return 
        
        if root.left == None and root.right == None:
            #leaf node
            binaryNumber+=str(root.val)
            self.sumOfBinaryNumbers += int(binaryNumber,2)
            return 
        
        binaryNumber += str(root.val)
        
        self.dfs(root.left, binaryNumber)
        self.dfs(root.right, binaryNumber)
