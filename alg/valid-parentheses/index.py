class Solution:
    def isValid(self, s: str) -> bool:
        brakets = {"(": ")", "[": "]", "{": "}"}
        stack = []

        def check(s):
            n = len(s)
            if n == 0:
                if len(stack) == 0:
                    return True
                else:
                    return False
            if s[0] in brakets:
                stack.append(s[0])
                return check(s[1:])
            else:
                open = stack.pop()
                if s[0] != brakets[open]:
                    return False
                return check(s[1:])
        return check(s)

sol = Solution()
print(sol.isValid('([]{}'))