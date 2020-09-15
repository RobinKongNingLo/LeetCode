class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        tmp = ""
        res = []
        wordDict = set(wordDict)
        self.dfs(s, tmp, res, wordDict)
        return res
        
    def dfs(self, s, tmp, res, wordDict):
        if self.wordBreakI(s, wordDict):
            if not s:
                res.append(tmp[:-1])
                return 
            for i in range(len(s)):
                if s[:i+1] in wordDict:
                    self.dfs(s[i+1:], tmp + s[:i+1] + " ", res, wordDict)
    
    def wordBreakI(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[0] = True
        wordDict = set(wordDict)
        for i in range(len(s)):
            for j in range(i, len(s)):
                if dp[i] and s[i: j+1] in wordDict:
                    dp[j+1] = True
                    
        return dp[-1]
        
    