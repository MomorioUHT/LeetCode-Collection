class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            reversed = int(str(x)[::-1])
            return reversed if reversed < 2147483648 else 0
        else:
            reversed = -int(str(x)[:0:-1])
            return reversed if reversed > -2147483648 else 0