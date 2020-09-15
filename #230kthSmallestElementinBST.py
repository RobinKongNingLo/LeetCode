class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        kthSmallest = 0
        while True:
            while root:
                stack.append(root)
                root = root.left
            node = stack.pop()
            kthSmallest += 1
            if kthSmallest == k:
                return node.val
            root = node.right