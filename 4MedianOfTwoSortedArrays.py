class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        if len(merged) == 1:
            return merged[0]
        if len(merged) == 0:
            return float(0)
        else:
            if len(merged)%2 == 0:
                x = merged[(len(merged)//2)-1]
                y = merged[len(merged)//2]
                return float((x+y)/2)
            if len(merged)%2 != 0:    
                return float(merged[len(merged)//2])