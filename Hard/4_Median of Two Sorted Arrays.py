class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=sorted(nums1+nums2)
        nums_len=len(nums)
        if nums_len % 2 is 0:
            return (nums[int(nums_len/2)-1]+nums[int(nums_len/2)])/2
        else:
            return nums[int(nums_len/2)]