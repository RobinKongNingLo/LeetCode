class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dict = {}
        minlen = len(s) + 1
        l = 0
        ans = ''
        for c in t:
            if c not in dict:
                dict.update({c:1})
            else:
                dict[c] += 1
        
        count = len(dict)
        for r in range(len(s)):
            if s[r] in dict:
                dict[s[r]] -= 1
                if dict[s[r]] == 0:
                    count -= 1
            else:
                continue
            
            while count == 0:
                if r - l + 1 <= minlen:
                    minlen = r - l + 1
                    ans = s[l:r+1]
                    
                
                if s[l] in dict:
                    dict[s[l]] += 1
                    if dict[s[l]] == 1:
                        count += 1
                
                l  += 1
        
        return ans
            
            
            