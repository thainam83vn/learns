#permute(nums) = [nums[0], permute(nums[1:])]
class Solution:
    def listExclude(self, ls, x):
        r = []
        for a in ls:
            if a != x:
                r = r + [a]
        return r

    def permute(self, nums: [int]) -> [[int]]:
        if len(nums) == 1:
            return [[nums[0]]]

        result = []
        for x in nums:
            r = self.permute(self.listExclude(nums, x))
            for y in r:
                result = result + [[x] + y]
        return result

data = [1,2,3]
sol = Solution()
print(sol.permute(data))
