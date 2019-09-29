class Solution:
    def maxValue(self, n):
        isNeg = n < 0
        s = str(abs(n))
        found = False
        r = ''
        for digit in s:
            if not found:
                if not isNeg and digit <= '5' or isNeg and digit >= '5':
                    r = r + '5' + digit
                    found = True
                else:
                    r = r + digit
            else:
                r = r + digit

        return ("-" if isNeg else "") + r

sol = Solution()
print(sol.maxValue(268))
print(sol.maxValue(670))
print(sol.maxValue(0))
print(sol.maxValue(-999))