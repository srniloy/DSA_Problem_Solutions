import heapq

class Solution(object):
    def resultingString(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        if n < 2:
            return s

        prev = list(range(-1, n - 1))
        next_ = list(range(1, n + 1))
        removed = set()
        heap = []

        def is_consecutive(a, b):
            diff = abs(ord(a) - ord(b))
            return diff == 1 or (a == 'a' and b == 'z') or (a == 'z' and b == 'a')

        # Initial scan for consecutive pairs
        for i in range(n - 1):
            if is_consecutive(s[i], s[i + 1]):
                heapq.heappush(heap, i)

        while heap:
            i = heapq.heappop(heap)
            if i in removed or (i + 1) in removed:
                continue
            if not (0 <= i < n and 0 <= i + 1 < n):
                continue
            if not is_consecutive(s[i], s[i + 1]):
                continue

            removed.add(i)
            removed.add(i + 1)

            p = prev[i]
            nxt = next_[i + 1]

            if p >= 0:
                next_[p] = nxt
            if nxt < n:
                prev[nxt] = p

            if p >= 0 and nxt < n and p not in removed and nxt not in removed:
                if is_consecutive(s[p], s[nxt]):
                    heapq.heappush(heap, p)

        result = []
        for i in range(n):
            if i not in removed:
                result.append(s[i])

        return ''.join(result)