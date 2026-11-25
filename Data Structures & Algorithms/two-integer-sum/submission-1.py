from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = defaultdict(int)
        for i,val in enumerate(nums):
            print (i,val)
            hashmap[val]=i
        for i,val in enumerate(nums):
            res=target-val
            if res in hashmap and i!=hashmap[res]:
                return(sorted([i,hashmap[res]]))
        
        