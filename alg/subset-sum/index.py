class Solution:
    def subsetSum(self, arr):
        n = len(arr)
        if n == 0:
            return True
        if n == 1:
            return False
        allsum = sum(arr)
        if allsum % 2 == 1:
            return False

        def subset(arr, sum):
            if sum == 0:
                return True
            if sum < 0:
                return False
            if len(arr) == 0 and sum > 0:
                return False
            return subset(arr[1:], sum - arr[0]) or subset(arr[1:], sum)

        return subset(arr, sum(arr) / 2)

sol = Solution()
print(sol.subsetSum([4,7,1,2,6,2]))