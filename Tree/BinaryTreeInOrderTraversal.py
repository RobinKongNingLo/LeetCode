class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        node = root
        while True:
            while node:
                stack.append(node)
                node = node.left
            if not stack:
                return res
            tmp = stack.pop()
            res.append(tmp.val)
            node = tmp.right
