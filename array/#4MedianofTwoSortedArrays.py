class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        while nums1 and nums2:
            if nums1[-1] >= nums2[-1]:
                nums3.append(nums1.pop())
            else:
                nums3.append(nums2.pop())
                
        if nums1: 
            nums1.reverse()
            nums3 += nums1
        if nums2:
            nums2.reverse()
            nums3 += nums2
        
        if len(nums3) %2 == 0: #Even number of elements
            return (nums3[len(nums3) // 2 - 1] + nums3[len(nums3) // 2]) / 2
            
        else:
            return nums3[len(nums3) // 2]
