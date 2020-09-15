class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0
        if not str[0].isdigit() and str[0] != '-' and str[0] != ' ' and str[0] != '+':
            return 0
        outstr = ''
        neg = False
        pos = False
        for char in str:
            if char == ' ' and not neg and not pos and not outstr:
                continue
            elif char == '+' and not neg and not pos and not outstr:
                pos = True
            elif char == '-' and not neg and not pos and not outstr:
                neg = True
            elif char.isdigit():
                outstr = outstr + char
            else:
                break
        if neg and outstr:
            outint = -int(outstr)
        elif not neg and outstr:
            outint = int(outstr)
        else:
            return 0
        
        if outint < -2**31:
            return -2147483648
        if outint > 2147483647:
            return 2147483647
        else:
            return outint