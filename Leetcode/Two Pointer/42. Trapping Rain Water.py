class Solution(object):
    def trap(self, height):
        lmax, rmax = [0 for i in range(len(height))], [0 for i in range(len(height))]
        lm, rm = 0, 0
        lmax[0] = 0
        for i in range(1, len(height)):
            if height[i-1] > lm:
                lm = height[i-1]
            lmax[i] = lm
        rmax[len(height)-1]=0
        for i in range(len(height)-2, 0, -1):
            if height[i + 1] > rm:
                rm = height[i + 1]
            rmax[i] = rm
        units = 0
        for i in range(len(height)):
            contains = min(lmax[i], rmax[i]) - height[i]
            units += contains if contains > 0 else 0
        return units


s = Solution()

s.trap([0,1,0,2,1,0,1,3,2,1,2,1])