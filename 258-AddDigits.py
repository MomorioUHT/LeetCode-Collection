class Solution:
    def SumOfDigits(num):
        x = 0
        for i in str(num):
            x += int(i)
        return x 
    def addDigits(self, num: int) -> int:
        while len(str(num)) != 1:
            num = Solution.SumOfDigits(num)
        return num