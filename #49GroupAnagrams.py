class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            #dict.get(key, []) will return [] if key doesn't exist, if call d[key] directly, there will be error 
            d[key] = d.get(key, []) + [w]
        return list(d.values())