class Solution:
    def maximalSquare(self, matrix: [[str]]) -> int:
        self.cache = [[0 for _ in row] for row in matrix]

        def find(matrix, n, m):
            if n <= 0 or m <= 0:
                return 0

            if n == 1 and m == 1:
                self.cache[n - 1][m - 1] = 1 if matrix[n - 1][m - 1] == '1' else 0
                return self.cache[n - 1][m - 1]

            plus = 1 if matrix[n - 1][m - 1] == '1' else 0
            top = find(matrix, n - 1, m)
            left = find(matrix, n, m - 1)
            cross = find(matrix, n - 1, m - 1)
            f = lambda a: a is not None
            values = [x for x in [top, left, cross] if f(x)]
            if len(values) > 0:
                self.cache[n - 1][m - 1] = plus + min(values)
            else:
                self.cache[n - 1][m - 1] = plus
            return self.cache[n - 1][m - 1]
        n = len(matrix)
        m = len(matrix[0]) if n > 0 else 0
        edge = find(matrix, n, m)
        maxEdge = 0
        for row in self.cache:
            for x in row:
                maxEdge = max(maxEdge, x)
        print(self.cache)
        return maxEdge**2

sol = Solution();
#print(sol.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
#print(sol.maximalSquare(['1','0']))
print(sol.maximalSquare([["1","0","1","1","0","1"],["1","1","1","1","1","1"],["0","1","1","0","1","1"],["1","1","1","0","1","0"],["0","1","1","1","1","1"],["1","1","0","1","1","1"]]))