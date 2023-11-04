class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = sorted(nums1 + nums2)
        print(merged)
        length = len(merged)
        if length %2 != 0:
            median = merged[length//2]
        else:
            left = merged[(length//2)-1]
            right = merged[(length//2)]
            median = (left+right)/2
        return median
        
