class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        ans = ""
        if numerator * denominator < 0:
            ans += "-"
        num, rem = divmod(abs(numerator), abs(denominator))
        if rem == 0:
            return ans + str(num)
        ans += str(num) + "."
        dict = {}
        dec = ""
        i = 0
        while True:
            
            if rem in dict:
                return ans + dec[:dict[rem]] + "(" + dec[dict[rem]:] + ")"
            dict[rem] = i
            
            num, rem = divmod(10 * rem, abs(denominator))
            if rem == 0:
                return ans + dec + str(num)
            
            dec += str(num)
            i += 1