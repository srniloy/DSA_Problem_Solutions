class Solution(object):
    def countBits(self, n):
        res = [0] * (n+1)
        offset = 1
        for i in range(1, n+1):
            if offset*2 == i:
                offset = i
            res[i] = 1 + res[i-offset]
        print(res)


s = Solution()
s.countBits(2)