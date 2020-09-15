class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            digits[-1] = 0
            carry = 1
            for i in range(2, len(digits) + 1):
                if digits[-i] == 9 and carry == 1:
                    digits[-i] = 0
                    carry = 1
                else:
                    digits[-i] += 1
                    carry = 0
                    break
            
            if carry == 1:
                digits = [1] + digits
            
        return digits