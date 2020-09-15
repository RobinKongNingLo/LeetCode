class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        table = [1, 1] + [0] * (len(s)-1)
        
        for i in range(2,len(s)+1):
            if s[i-1] == '0':
                if int(s[i-2:i]) == 10 or int(s[i-2:i]) == 20:
                    table[i] = table[i-2]
                else:
                    return 0
            elif 10 < int(s[i-2:i]) <= 26:
                table[i] = table[i-1] + table[i-2]
            else:
                table[i] = table[i-1]
        return table[-1]
            
            