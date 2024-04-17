class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = []
        for i in range(1,arr[-1]):
            if i not in arr:
                missing.append(i)
        for j in range(arr[-1]+1,2001):
            missing.append(j)
        return missing[k-1]