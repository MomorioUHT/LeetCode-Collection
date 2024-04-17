class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #Right to left 
        i = len(s) - 1
        lastlength = 0
        while s[i] == " ":
            i -= 1
        while i >= 0 and s[i] != " ":
            lastlength += 1
            i -= 1
        return lastlength