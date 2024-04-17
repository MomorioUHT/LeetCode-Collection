class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1: return s
        
        length = len(s)
        longest = ''
        for i in range(length):
            for j in range(i, length):
                curr = s[i:j+1]
                if (curr == curr[::-1]):
                    if len(curr) > len(longest): 
                        longest = curr

        return longest