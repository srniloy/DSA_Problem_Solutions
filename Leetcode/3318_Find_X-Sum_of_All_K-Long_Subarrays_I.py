
class Solution(object):

    def findXSum(self, nums, k, x):

        def xSum(wDict):
            wSorted = sorted(wDict.items(), key=lambda item: (-item[1], -item[0]))
            i=1
            res = 0
            for v in wSorted:
                if i > x:
                    break
                res += v[0] * v[1]
                i+=1
            return res

        arr = []
        for i in range(len(nums)-k+1):
            cArr = {}
            window = nums[i:(i+k)]
            for v in window:
                cArr[v] = cArr.get(v, 0) + 1
            arr.append(xSum(cArr))
        return arr





s = Solution()
print(s.findXSum([1,1,2,2,3,4,2,3], 6, 2))