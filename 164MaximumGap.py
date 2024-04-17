class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        temp = []
        if len(nums) < 2:
            temp.append(0)
        if len(nums) >= 2:
            for i in range(1,len(nums)):
                if nums[i]-nums[i-1] not in temp:
                        temp.append(nums[i]-nums[i-1])
        ans = max(temp)
        return ans