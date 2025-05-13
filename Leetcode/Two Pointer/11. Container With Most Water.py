class Solution(object):
    def maxArea(self, h):
        l, r = 0, len(h)-1
        maxA = 0

        while l <= r:
            if h[l] < h[r]:
                area = h[l]*(r-l)
                l += 1
            else:
                area = h[r] * (r - l)
                r -= 1
            if area > maxA:
                maxA = area
        return maxA


print(Solution().maxArea([1,8,6,2,5,4,8,3,7]))