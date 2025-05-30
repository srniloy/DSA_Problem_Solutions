from collections import defaultdict

class Solution:
    def maxSubstrings(self, word: str) -> int:

        ci = defaultdict(list)
        for i, c in enumerate(word):
            ci[c].append(i)

        intervals = []

        for c in ci:
            indices = ci[c]
            if len(indices) < 2:
                continue
            for i in range(len(indices)):
                for j in range(i + 1, len(indices)):
                    start = indices[i]
                    end = indices[j]
                    if end - start + 1 >= 4:
                        intervals.append((start, end))

        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        count = 0
        last_end = -1
        for start, end in intervals:
            if start > last_end:
                count += 1
                last_end = end

        return count

s = Solution()
print(s.maxSubstrings("abcdeafdef"))