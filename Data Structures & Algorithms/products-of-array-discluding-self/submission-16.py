class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        
        prefix = [1]*length
        product = 1
        for i in range(length):
            prefix[i] = product
            product *= nums[i]
        
        suffix = [1]*length
        product = 1        
        for i in range(length-1, -1, -1):
            suffix[i] = product
            product *= nums[i]
    
        for i in range(length):
            prefix[i]*=suffix[i]


        return prefix