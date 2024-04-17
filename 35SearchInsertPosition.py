class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        x = 0
        for i in range(len(nums)):
            if nums[i] == target:
                x = i
            if nums[i-1] < target < nums[i]:
                x = i
            if nums[-1] < target:
                x = len(nums)
        return int(x)