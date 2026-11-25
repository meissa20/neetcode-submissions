class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = {}
        for n in nums:
            x = freq.get(n,0)
            if x != 0:
                return True
            freq[n] = x + 1
        return False

nums = [1, 2, 3, 3]
solution = Solution()
print(solution.hasDuplicate(nums))