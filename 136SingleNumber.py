class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        check = {}
        for i in nums:
            if i not in check:
                check[i] = 0
            check[i] += 1
        print(check)
        for j in check:
            if check[j] == 1:
                return j