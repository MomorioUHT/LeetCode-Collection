class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        res = []
        for x in nums:
            if x not in count:
                count[x] = 0
            if x in count:
                count[x] += 1
        for y in count:
            if count[y] > len(nums)//3:
                res.append(y)
        return res