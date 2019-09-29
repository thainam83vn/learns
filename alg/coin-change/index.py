class Solution:
    def coin(self, arr, i, sum):
        if sum == 0:
            return 1
        if sum < 0 or sum > 0 and i>len(arr) - 1:
            return 0
        count = 0
        x = 0
        while sum >= arr[i] * x:
            count += self.coin(arr, i + 1, sum - arr[i] * x)
            x += 1
        return count

sol = Solution()
#print(sol.coin([1,3,5,7], 0,8))
print(sol.coin([1,2,3], 0,4))