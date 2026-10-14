class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        string = ""
        for i in digits:
            string += str(i)
        x = int(string) + 1
        list = []
        for j in str(x):
            list.append(int(j))
        return list