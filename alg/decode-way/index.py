class Solution:
    def isCorrectCode(self, s) -> bool:
        if len(s) == 0:
            return False
        if s[0] <= '0' or s[0] > '9':
            return False
        if len(s) == 2:
            if s[0] > '2' or s[0] == '2' and s[1] > '6':
                return False
        return True

    def numDecodings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 1
        if n == 1 and self.isCorrectCode(s):
            return 1
        r1, r2 = 0, 0
        if self.isCorrectCode(s[:1]):
            r1 = self.numDecodings(s[1:])
        if self.isCorrectCode(s[:2]):
            r2 = self.numDecodings(s[2:])
        return r1 + r2


sol = Solution()
print(sol.numDecodings('0'))