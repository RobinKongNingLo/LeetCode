class Solution:
    def isPalindrome(self, s: str) -> bool:
        #Keep only alphabets in s, change capital to lowercase
        sNew = ''
        for char in s:
            if (ord(char) >= 97 and ord(char) <= 122) or char.isdigit():
                sNew += char
            elif (ord(char) >= 65 and ord(char) <= 90):
                sNew += char.lower()
            else:
                continue
        l = 0
        r = len(sNew) - 1
        while l <= r:
            if sNew[l] == sNew[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
        