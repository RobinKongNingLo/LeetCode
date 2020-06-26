class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if(p==None and q==None):
            return True
        if(p!=None and q!=None):
            a=self.isSameTree(p.left,q.left)
            b=self.isSameTree(p.right,q.right)
            return(p.val==q.val and a and b)
        return False
