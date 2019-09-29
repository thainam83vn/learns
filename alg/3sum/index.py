class Solution:
    def threeSum(self, nums: []) -> [[]]:
        n = len(nums)
        if n == 0:
            return []
        sums = {}
        results = set()
        for i in range(n):
            for j in range(i, n):
                if i != j:
                    sum = nums[i] + nums[j]
                    if sum not in sums:
                        sums[sum] = [[i, j]]
                    else:
                        sums[sum] = sums[sum] + [[i, j]]
        #print(sums)
        for k in range(n):
            if -nums[k] in sums:
                for indexes in sums[-nums[k]]:
                    if k not in indexes:
                        results.add((nums[k], nums[indexes[0]], nums[indexes[1]]))
        return results



sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4]))
print(sol.threeSum([-7,-11,12,-15,14,4,4,11,-11,2,-8,5,8,14,0,3,2,3,-3,-15,-2,3,6,1,2,8,-5,-7,3,1,8,11,-3,6,3,-4,-13,-15,14,-8,2,-8,4,-13,13,11,5,0,0,9,-8,5,-2,14,-9,-15,-1,-6,-15,9,10,9,-2,-8,-8,-14,-5,-14,-14,-6,-15,-5,-7,5,-11,14,-7,2,-9,0,-4,-1,-9,9,-10,-11,1,-4,-2,2,-9,-15,-12,-4,-8,-5,-11,-6,-4,-9,-4,-3,-7,4,9,-2,-5,-13,7,2,-5,-12,-14,1,13,-9,-3,-9,2,3,8,0,3]))