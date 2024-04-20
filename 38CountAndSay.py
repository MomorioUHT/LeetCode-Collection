class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"

        result = ""
        prev_result = self.countAndSay(n-1)

        count = 1
        for i in range(0,len(prev_result)):
            if i + 1 < len(prev_result) and prev_result[i+1] == prev_result[i]:
                count += 1
            else:
                result += str(count) + prev_result[i]
                count = 1
        return result
