class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needlen = len(needle)
        for i in range(len(haystack) - needlen + 1):
            if haystack[i:i+needlen] == needle:
                return i
        
        return -1