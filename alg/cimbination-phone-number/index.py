class Solution:
    def letterCombinations(self, digits):
        map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        cache = {}
        def combine(digits):
            n = len(digits)
            if n == 0:
                cache[digits] = ""
                return
            if n == 1:
                cache[digits] = [c for c in map[digits]]
                return

            rs = []
            for c in map[digits[0]]:
                sub = digits[1:]
                combine(sub)
                combines = cache[sub]
                for r in combines:
                    rs = rs + [c + r]
            cache[digits] = rs
        combine(digits)
        return cache[digits]

sol = Solution()
print(sol.letterCombinations("23"))