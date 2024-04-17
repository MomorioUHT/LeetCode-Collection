class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        x = set(nums)
        i = 1
        while i in x:
            i += 1
        return i