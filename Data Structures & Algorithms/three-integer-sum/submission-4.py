class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)
        length = len(nums)
        l = 0
        r = length - 1
        for i in range(length):
            val = 0 - nums[i]
            l = i+1
            r = length - 1
            while l < r:
                s = nums[l] + nums[r]
                # print(f"s: {s} val: {val} l: {l}")
                if s > val:
                    r-=1
                elif s < val:
                    l+=1
                else:
                    x = [nums[i], nums[l], nums[r]]
                    x.sort()
                    if x not in res:
                        res.append(x)
                    l+=1
                    r-=1

        return res
                    