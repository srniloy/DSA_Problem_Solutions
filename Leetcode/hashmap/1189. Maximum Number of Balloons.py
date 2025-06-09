class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text)
        countB = Counter('balloon')
        res = len(text)
        for c in countB:
            res = min(res, countText[c] // countB[c])
        return res