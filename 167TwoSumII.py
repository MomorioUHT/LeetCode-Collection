class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1
        while True:
            sol = numbers[l]+numbers[r]
            if sol > target:
                r -= 1
            elif sol < target:
                l += 1
            elif sol == target:
                return [l+1,r+1]