class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #merged nums1 and nums 2 is nums3
        nums3 = []
        while nums1 and nums2:
            if nums2[-1] > nums1[-1]:
                nums3.append(nums2.pop())
            else:
                nums3.append(nums1.pop())
        if nums1:
            nums1.reverse()
            nums3 = nums3 + nums1
        if nums2:
            nums2.reverse()
            nums3 = nums3 + nums2
        if len(nums3) % 2 == 0:
            median = (nums3[(len(nums3)//2)] + nums3[(len(nums3)//2-1)]) / 2
        else:
            median = nums3[len(nums3)//2]
        return median