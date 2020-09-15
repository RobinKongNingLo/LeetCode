class Solution:
    def longestPalindrome(self, s: str) -> str:
        out = ''
        for i in range(len(s)):
            #Case 1: s[i] in the center e.g.'aba'
            temp = self.findPalidromic(s, i, i)
            if len(temp) > len(out):
                out = temp
            #Case 2: s[i] and s[i+1] are the same and both in the center e.g. 'abba'
            temp = self.findPalidromic(s, i, i+1)
            if len(temp) > len(out):
                out = temp
        return out
    def findPalidromic(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]