class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        self.haveOne(root)
        return root
        
    def haveOne(self, root):
        if not root: 
            return False
        left = self.haveOne(root.left)
        right = self.haveOne(root.right)
        if not left:
            root.left = None
        if not right:
            root.right = None
        return root.val or left or right
