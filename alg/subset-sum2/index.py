class Solution:
    def sss(self, arr, sum):
        if sum == 0:
            return True
        if sum < 0 or sum > 0 and len(arr) == 0:
            return False
        return self.sss(arr[1:], sum - arr[0]) or self.sss(arr[1:], sum)

sol = Solution()
print(sol.sss([7,3,2,5,8], 30))