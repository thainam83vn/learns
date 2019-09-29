class Solution(object):
    def binaryGap(self, N):
        A = [i for i in range(32) if (N >> i) & 1]
        print(A)
        if len(A) < 2: return 0
        return max(A[i+1] - A[i] for i in range(len(A) - 1))

sol = Solution()
print(sol.binaryGap(5))