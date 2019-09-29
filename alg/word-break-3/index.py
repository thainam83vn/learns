class Solution:
    def wordBreak(self, s: str, wordDict: [str]):
        mem = {}
        def process(s: str):
            n = len(s)
            if n == 0:
                return 0
            if s in mem:
                return mem[s]

            a = ""
            minWords = -1
            for i in range(n):
                a = a + s[i]
                if a in wordDict:
                    ra = process(s[i+1:])
                    if ra is not None:
                        if minWords==-1 or minWords < ra + 1:
                            minWords = ra + 1
            mem[s] = minWords
            return mem[s]
        return process(s)

sol = Solution()
print(sol.wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"]))
print(sol.wordBreak('pineapplepenapple', ["apple", "pen", "applepen", "pine", "pineapple"]))
print(sol.wordBreak("aaaaaaa", ["aaaa","aa","a"]))