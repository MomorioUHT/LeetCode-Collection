class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needlength = len(needle)
        for i in range(len(haystack)):
            if haystack[i:needlength+i]==needle:
                return i
        else:
            return -1