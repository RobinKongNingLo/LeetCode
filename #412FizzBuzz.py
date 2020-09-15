class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        i = 1
        while i <= n:
            if i % 3 and i % 5:
                res.append(str(i))
            else:
                string = ''
                if i % 3 == 0:
                    string += 'Fizz'
                if i % 5 == 0:
                    string += 'Buzz'
                res.append(string)
            i += 1
        return res