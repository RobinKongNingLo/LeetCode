class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.helper(res, n, n)
        return res
    
    def helper(self, res, left, right, current = ''):
        #Goal
        if left == 0 and right == 0:
            res.append(current)
        #When number of rest left bracket and right bracket are equal, can only add '('
        if left == right:
            self.helper(res, left-1, right, current + '(')
        #When number of rest left beacket less than right bracket, cna add '(' or ')'
        if left < right:
            self.helper(res, left-1, right, current + '(')
            self.helper(res, left, right-1, current + ')')