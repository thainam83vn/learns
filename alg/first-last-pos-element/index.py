class Solution:
    #nums is sorted
    def find(self, nums: [int], target) -> []:
        if len(nums) == 0:
            return [-1, -1]
        def findIndex(nums: [], l, r, target):
            if l > r:
                return -1
            if l == r:
                if nums[l] == target:
                    return l
                else:
                    return -1
            m = (l + r) // 2
            #print('m {} {}=={}'.format(m, nums[m], target))
            if nums[m] == target:
                return m
            elif nums[m] > target:
                return findIndex(nums, l, m - 1, target)
            else:
                return findIndex(nums, m + 1, r, target)
        i = findIndex(nums, 0, len(nums) - 1, target)
        if i < 0:
            return [-1, -1]
        begin = end = i
        #print(i)
        while begin >= 0 and nums[begin] == target:
            begin -= 1
        while end < len(nums) and nums[end] == target:
            end += 1
        return [begin + 1, end - 1]


sol = Solution()
#print(sol.find([5,7,7,8,8,10], 8))
#print(sol.find([5,7,7,8,8,10], 6))
print(sol.find([5,5,5,5], 5))