class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if val==root.val:
            return root
        if val<root.val and root.left==None:
            return None
        if val>root.val and root.right==None:
            return None
        if val > root.val:
            return self.searchBST(root.right,val)
        if val < root.val:
            return self.searchBST(root.left,val)
