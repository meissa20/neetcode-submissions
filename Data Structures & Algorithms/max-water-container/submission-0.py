class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        l = 0
        r = length - 1
        maxi = 0
        while l < r:
            left = heights[l]
            right = heights[r]
            s = min(left, right) * (r - l)
            if maxi < s:
                maxi = s
            if left > right:
                r-=1
            else:
                l+=1
        return maxi

        