class Solution:
    def myAtoi(self, s: str) -> int:
        if s.isspace() or len(s) == 0: return 0

        numbers = ''
        s = s.strip()
        
        if s[0] == "-": sign = -1
        else: sign = 1

        if s[0] == "-" or s[0] == "+": s = s[1::]
        
        for i in s:
            if i.isdigit(): numbers += i
            else: break
                
        if numbers == '': return 0

        result = int(numbers) * sign
        if sign == -1: return max(-2147483648, result)
        return min(result, 2147483647)