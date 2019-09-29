class Solution:
    def __init__(self):
        self.cache = {}
    def knapsack(self, v, w, W):
        n = len(v)
        if W <= 0 or n == 0:
            return 0
        if n in self.cache:
            return self.cache[n]

        include = 0
        if W >= w[0]:
            include = self.knapsack(v[1:], w[1:], W - w[0]) + v[0]
        exclude = self.knapsack(v[1:], w[1:], W)
        self.cache[n] = max(include, exclude)
        return self.cache[n]

sol = Solution()
print(sol.knapsack([20,5,10,40,15,25], [1,2,3,8,7,4], 10))
print(sol.cache)
