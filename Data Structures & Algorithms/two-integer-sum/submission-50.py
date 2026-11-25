class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in freq:
                return [freq[diff], i]
            freq[val] = i