class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        currlv = [root]
        while currlv[0]:
            nxtlv = []
            for i in range(0,len(currlv)-1):
                nxtlv.append(currlv[i].left)
                nxtlv.append(currlv[i].right)
                currlv[i].next = currlv[i+1]
            nxtlv.append(currlv[-1].left)
            nxtlv.append(currlv[-1].right)
            currlv = nxtlv
        return root