class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        output = []
        curlev = [root]
        order = 1
        while curlev:
            vallevel = []
            nextlev = []
            for node in curlev:
                if node.left:
                    nextlev.append(node.left)
                if node.right:
                    nextlev.append(node.right)
                vallevel.append(node.val)
            if order < 0:
                vallevel = vallevel[::-1]
            output.append(vallevel)
            curlev = nextlev
            order = -order
            
        return output
#Alternative solution:    
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        output = []
        curlev = [root]
        order = 1
        while curlev:
            vallevel = []
            nextlev = []
            for node in curlev:
                if order < 0:
                    if node.right:
                        nextlev = [node.right] + nextlev
                    if node.left:
                        nextlev = [node.left] + nextlev
                else:
                    if node.left:
                        nextlev = [node.left] + nextlev
                    if node.right:
                        nextlev = [node.right] + nextlev
                    
                vallevel.append(node.val)
                
            output.append(vallevel)
            curlev = nextlev
            order = -order
            
        return output