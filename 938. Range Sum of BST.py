class Solution:
    def __init__(self):
        self.sumBetweenRange=0
        self.queue=[]
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.queue.append(root)
        return self.bfs(L, R)
    
    def bfs(self, L: int, R: int)-> int:
        
        root=self.queue.pop(0)
        
        if root==None and len(self.queue)!=0:
            self.bfs(L, R)
        if root==None:
            return None
   
        if L<=root.val<=R:
            self.sumBetweenRange+=root.val
        self.queue.append(root.left)
        self.queue.append(root.right)
        self.bfs(L, R)
        
        return self.sumBetweenRange
