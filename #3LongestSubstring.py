class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        substr = ""
        for char in s:
            if char in substr:
                substr = substr[substr.find(char) + 1: ]
            else:
                maxlen = max(maxlen, len(substr) + 1)
            substr = substr + char
        return maxlen