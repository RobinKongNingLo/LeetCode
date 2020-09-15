class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')':'(', ']':'[', '}':'{'}
        out = True
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            elif stack:
                lastchar = stack.pop()
                if match[char] != lastchar:
                    return False
            else:
                return False
            
        return not stack