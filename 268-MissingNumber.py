class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        list2 = []
        for i in range(0, len(nums)+1):
            list2.append(i)
            i += 1
        z = list(set(list2) - set(nums))
        for i in range(0, len(z)):
            return z[i]