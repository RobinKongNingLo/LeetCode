# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        nodes = [root] #Store tree nodes in the list called nodes
        res = [root.val]
        i = 0
        while i < len(nodes):
            if nodes[i].left:
                nodes.append(nodes[i].left)
                res.append(nodes[i].left.val)
            else:
                res.append(None)
            if nodes[i].right:
                nodes.append(nodes[i].right)
                res.append(nodes[i].right.val)
            else:
                res.append(None)
            i += 1
        return res
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        root = TreeNode(data[0])
        nodes = [root]
        i = 0
        j = 1
        while i < len(nodes):
            if j < len(data):
                if data[j] != None: 
                    nodes[i].left = TreeNode(data[j])
                    nodes.append(nodes[i].left)
                j += 1
                
            if j < len(data):
                if data[j] != None:
                    nodes[i].right = TreeNode(data[j])
                    nodes.append(nodes[i].right)
                j += 1
            i += 1
        return root
            

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))