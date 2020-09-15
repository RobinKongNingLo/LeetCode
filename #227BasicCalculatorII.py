class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = ""
        i = 0
        while i < len(s):
            if str.isdigit(s[i]):
                num += s[i]
                i += 1
            elif s[i] == "+" or s[i] == "-":
                if num:
                    stack.append(int(num))
                num = ""
                stack.append(s[i])
                i += 1
            elif s[i] == "*":
                newnum = ""
                i += 1
                while i < len(s) and (str.isdigit(s[i]) or s[i] == " "):
                    if str.isdigit(s[i]):
                        newnum += s[i]
                    i += 1
                if num:
                    stack.append(int(num))
                stack[-1] = stack[-1] * int(newnum)
                num = ""
            elif s[i] == "/":
                newnum = ""
                i += 1
                while i < len(s) and (str.isdigit(s[i]) or s[i] == " "):
                    if str.isdigit(s[i]):
                        newnum += s[i]
                    i += 1
                if num:
                    stack.append(int(num))
                stack[-1] = int(stack[-1] / int(newnum))
                num = ""
            else:
                i += 1
        if num:
            stack.append(int(num))
        res = self.calcStack(stack)
        return int(res)
    
    def calcStack(self, stack):
        if len(stack) == 1:
            return stack[0]
        i = 1
        res = stack[0]
        while i < len(stack):
            if stack[i] == "+":
                res += stack[i+1]
                i += 2
            elif stack[i] == "-":
                res -= stack[i+1]
                i += 2
        return res