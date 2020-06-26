class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.sumPath(root, 0)
        return self.res
        
    def sumPath(self, root, path):
        path = path * 10 + root.val
        if root.left:
            self.sumPath(root.left, path)
        if root.right:
            self.sumPath(root.right, path)
        if not root.left and not root.right:
            self.res += path
            return
