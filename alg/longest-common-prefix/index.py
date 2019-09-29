import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = strs[0]
        for s in strs:
            minLen = min(minLen, len(s))
        return minLen