from libs.tree import TreeLibs, TreeNode

class Solution:
    def travelLevelFirst(self, root):
        levels = {}
        def save(value, level):
            if level not in levels:
                levels[level] = []
            levels[level] = levels[level] + [value]

        def travel(root, level):
            if root is None:
                save(None, level)
                return
            save(root.val, level)
            travel(root.left, level + 1)
            travel(root.right, level + 1)
        travel(root, 0)
        result = []
        for key in levels.keys():
            result = result + levels[key]
        return result

    def findIndex(self, arr, val):
        for i in range(len(arr)):
            if arr[i] == val:
                return i
        return -1

    def firstRight(self, root, val):
        arr = self.travelLevelFirst(root)
        i = self.findIndex(arr, val)
        j = i + 1
        while j < len(arr) and arr[j] is None:
            j += 1
        return arr[j]

sol = Solution()
libs = TreeLibs()
tree = libs.createBinaryTree([0, 1, 2, 3, None, None, 4])
print(sol.firstRight(tree, 3))