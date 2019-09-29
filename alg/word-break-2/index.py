class Solution:
    def wordBreak(self, s: str, wordDict: [str]):
        mem = {}
        result = {}
        def process(s: str):
            n = len(s)
            if n == 0:
                return []
            if s in mem:
                return mem[s]

            a = ""
            rProcess = []
            for i in range(n):
                a = a + s[i]
                if a in wordDict:
                    ra = process(s[i+1:])
                    if ra is not None:
                        if len(ra) > 0:
                            for x in ra:
                                rProcess = rProcess + [a + ' ' + x]
                        else:
                            rProcess = [a]
                        mem[s] = rProcess
            if s not in mem:
                mem[s] = None
            return mem[s]
        return process(s)

sol = Solution()
#print(sol.wordBreak('catsanddog', ["cat", "cats", "and", "sand", "dog"]))
#print(sol.wordBreak('pineapplepenapple', ["apple", "pen", "applepen", "pine", "pineapple"]))
print(sol.wordBreak("aaaaaaa", ["aaaa","aa","a"]))