from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramMap = defaultdict(list)
        result = []
        for s in strs:
            sorted_s = tuple(sorted(s))
            anagramMap[sorted_s].append(s)
        for val in anagramMap.values():
            result.append(val)
        return result