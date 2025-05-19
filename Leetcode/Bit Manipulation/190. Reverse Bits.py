class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for i in range(32):
            lsb = n & 1
            res = res | (lsb << (31-i))
            n = n >> 1
        return res

print(Solution().reverseBits(int('00000010100101000001111010011100', 2)))
