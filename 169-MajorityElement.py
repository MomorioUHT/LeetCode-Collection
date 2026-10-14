class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        x = 0
        if len(nums)%2 == 0:
            x = nums[int(len(nums)/2)]
            return x
        if len(nums)%2 != 0:
            x = nums[int(len(nums)//2)]
            return x
        if len(nums) == 0:
            return int(0)
        if len(nums) == 1:
            return int(nums[0])