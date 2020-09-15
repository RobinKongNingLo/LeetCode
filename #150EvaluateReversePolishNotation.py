class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = {"+":(lambda x,y: x+y), "-":(lambda x,y: y-x), "*":(lambda x,y: x*y), "/":(lambda x,y: int(y/x))}
        stack = []
        for token in tokens:
            if token in ops:
                stack.append(ops[token](stack.pop(),stack.pop()))
            else:
                stack.append(int(token))
        return stack[-1]