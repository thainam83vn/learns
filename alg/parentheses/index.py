class Solution:
    def generateParenthesis(self, n: int) -> [str]:
        if n == 1:
            return ['()']
        result = []
        children = self.generateParenthesis(n - 1)
        for s in children:
            for a in ['(' + s + ')', '()' + s, s + '()']:
                if a not in result:
                    result = result + [a]
        return result

sol = Solution()
print(sol.generateParenthesis(4))
