class Solution:
    def combinationSum(self, c, t):
        dp = [[[] for _ in range(len(c))] for _ in range(t + 1)]
        for n in range(1, t + 1):
            for i, a in enumerate(c):
                if n == a:
                    dp[n][i].append([a])
                else:
                    if n - a < 0: continue
                    for b in dp[n - a][i:]:
                        for s in b:
                            dp[n][i].append([a, *s])
        print(dp)
        return [s for b in dp[-1] for s in b]

sol = Solution()
print(sol.combinationSum([2, 3, 6, 7], 7))
