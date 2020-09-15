class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.res = set([])
        self.root = {}
        #Build the Trie
        for word in words:
            node = self.root
            for char in word:
                if char not in node:
                    node[char] = {}
                    node = node[char]
                else:
                    node = node[char]
            node["*"] = word
            
        #Find words
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, self.root)
       
        return self.res
    
    def dfs(self, board, i, j, node):
        for children in node:
            if children == "*":
                self.res.add(node[children])
                continue
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or children != board[i][j]:
                continue
            board[i][j] = 0
            self.dfs(board, i-1, j, node[children])
            self.dfs(board, i+1, j, node[children])
            self.dfs(board, i, j-1, node[children])
            self.dfs(board, i, j+1, node[children])
            board[i][j] = children