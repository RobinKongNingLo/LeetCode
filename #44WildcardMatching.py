class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #Initialize
        s = ' ' + s
        p = ' ' + p
        T = [[0]*(len(s)) for i in range(len(p))]
        T[0][0] = 1
        
        for i in range(1,len(p)):
            #When j=0
            if p[i] == '*':
                T[i][0] = T[i-1][0]
            for j in range(1, len(s)):
                if p[i] == '*':
                    T[i][j] = T[i-1][j] or T[i][j-1]
                elif p[i] == '?':
                    T[i][j] = T[i-1][j-1]
                else:
                    if p[i] == s[j]:
                        T[i][j] = T[i-1][j-1]
        
        return T[-1][-1]