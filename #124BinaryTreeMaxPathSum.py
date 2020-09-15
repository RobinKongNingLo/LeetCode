class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        sums = []
        #Maximum path sum starting from root
        maxPathRoot = self.help(root, sums)
        return max(sums)
    
    def help(self, root, sums):
        if not root:
            return 0
        leftPath = self.help(root.left, sums)
        rightPath = self.help(root.right, sums)
        maxPath = max(root.val + leftPath, root.val + rightPath, root.val)
        sums.append(max(root.val + leftPath + rightPath, maxPath))
        return maxPath