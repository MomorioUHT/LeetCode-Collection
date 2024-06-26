class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        x = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                nums[x], nums[i] = nums[i], nums[x]
                x += 1
        return nums