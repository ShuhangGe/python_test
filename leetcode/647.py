from types import str

class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False]*len(s) for _ in range(len(s))]
        result = 0
        for i range(0,len(s)-1):
            for j in range(i, len(s)):
                