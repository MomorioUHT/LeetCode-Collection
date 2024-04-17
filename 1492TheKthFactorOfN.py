class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ans = []
        ans.append(n)
        for i in range(1,n):
            if n%i == 0:
                ans.append(i)
        ans.sort()
        if k <= len(ans):
            return ans[k-1]
        if k > len(ans):
            return -1