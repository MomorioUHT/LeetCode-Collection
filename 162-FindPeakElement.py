class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxint = max(nums)
        for i in range(0,len(nums)):
            if maxint == nums[i]:
                return i