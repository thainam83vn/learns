class Solution:
    def __init__(self, badVersion):
        self.badVersion = badVersion

    def isBadVersion(self, v) -> bool:
        return v >= self.badVersion

    def firstBad(self, l, r) -> int:
        if l == r:
            return l
        m = int((l+r)/2)
        if self.isBadVersion(m):
            return self.firstBad(l, m - 1)
        else:
            return self.firstBad(m + 1, r)

sol = Solution(101)
print(sol.firstBad(1, 10000))