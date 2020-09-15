class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        output = []
        curlev = [root]
        while curlev:
            vallevel = []
            nextlev = []
            for node in curlev:
                if node.left:
                    nextlev.append(node.left)
                if node.right:
                    nextlev.append(node.right)
                vallevel.append(node.val)
            output.append(vallevel)
            curlev = nextlev
            
        return output
            