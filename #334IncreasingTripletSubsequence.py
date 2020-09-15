import random
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
        
        #Find k most frequent elements
        k_largest = self.find_k_largest(dict, k)
        return list(k_largest.keys())
        
    def find_k_largest(self, dict, k):
        pivot = random.choice(list(dict.values()))
        left = {}
        right = {}
        for entry in dict:
            if dict[entry] < pivot:
                left[entry] = dict[entry]
            else:
                right[entry] = dict[entry]
        if len(right) == k:
            return right
        if len(right) > k:
            return self.find_k_largest(right, k)
        return {**right, **self.find_k_largest(left, k - len(right))}