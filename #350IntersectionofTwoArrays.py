class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dict1 = {}
        dict2 = {}
        for num in nums1:
            if num in dict1:
                dict1[num] += 1
            else:
                dict1[num] = 1
        for num in nums2:
            if num in dict2:
                dict2[num] += 1
            else:
                dict2[num] = 1
        res = []
        for key in dict1:
            if key in dict2:
                res += [key] * min(dict1[key], dict2[key])
        return res