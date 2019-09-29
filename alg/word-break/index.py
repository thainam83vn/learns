class Solution:
    def wordBreak(self, s: str, wordDict: [str]) -> bool:
        mem = {}
        def process(s: str):
            n = len(s)
            if n == 0:
                return True
            if s in mem:
                return mem[s]

            a = ""
            for i in range(n):
                a = a + s[i]
                if a in wordDict:
                    r = process(s[i+1:])
                    if r:
                        mem[s] = r
                        return r
            mem[s] = False
            return False
        return process(s)

sol = Solution()
print(sol.wordBreak('leetcode', ['leet', 'code']))
print(sol.wordBreak('applepenapple', ["apple", "pen"]))
print(sol.wordBreak('catsandog', ["cats", "dog", "sand", "and", "cat"]))