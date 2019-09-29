import sys
from libs.tree import TreeNode, TreeLibs

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        self.result = {}
        self.maxV = 0
        self.maxL = -1
        def add(level, val):
            if level not in self.result:
                self.result[level] = val
            else:
                self.result[level] += val

            if self.maxV < self.result[level]:
                self.maxV = self.result[level]
                self.maxL = level

        def travel(root, level):
            if root is None:
                add(level, 0)
                return
            add(level, root.val)
            travel(root.left, level + 1)
            travel(root.right, level + 1)
        travel(root, 0)
        return self.result

libs = TreeLibs()
tree = libs.createBinaryTree([1, 7, 0, 7, -8, None, None])
sol = Solution()
print(sol.maxLevelSum(tree))

