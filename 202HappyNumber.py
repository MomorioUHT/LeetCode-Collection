
class Solution:
    def isHappy(self, n: int) -> bool:
        set1 = set()
        while n != 1:
            sum = 0
            for i in str(n):
                sum += int(i)**2
            n = sum
            if n in set1:
                return False
            else:
                set1.add(n)
        return True