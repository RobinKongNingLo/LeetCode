class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        res = []
        nextlevel = []
        level = [root]
        while level:
            tmp = []
            nextlevel = []
            for node in level:
                if node.left:
                    nextlevel.append(node.left)
                if node.right:
                    nextlevel.append(node.right)
                tmp.append(node.val)
            res.append(tmp)
            level = nextlevel
        return res
