class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                if target == nums[i] + nums[j] and i != j:
                    answer = []
                    answer.append(i)
                    answer.append(j)
                    return answer