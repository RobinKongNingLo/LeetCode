class Solution:
    def reverse(self, x: int) -> int:
        instr = str(x)
        outstr = ""
        for i in range(len(instr)):
            char = instr[len(instr) - i - 1]
            if i == 0 and char == '0':
                continue
            elif char == '-':
                outstr = char + outstr
            else:
                outstr += char
        
        try:
            outint = int(outstr)
            if outint <= 2**31-1 and outint >= -2**31:
                return outint
            else:
                return 0
            
        except ValueError:
            return 0