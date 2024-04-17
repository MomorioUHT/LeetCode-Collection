class Solution:
    def mySqrt(self, x: int) -> int:
        if x== 0 or x == 1:
            return x 

        start = 1
        end = x 

        while start <= end:
            mid = (start + end)//2
            mid_check  = mid * mid
            if mid_check == x:
                return mid
            if mid_check < x:
                start = mid+1
                answer = mid
            else:
                end = mid-1
        
        return answer