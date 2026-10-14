class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ": return True
        result = [i.lower() for i in s if i.isalnum()]
        return (result[::-1] == result)