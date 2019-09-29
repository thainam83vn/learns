from libs.tree import TreeNode, TreeLibs

class Solution:
    def delNodes(self, root: TreeNode, to_delete: [int]) -> [TreeNode]:
        self.nodes = []

        def travel(root, parent):
            if root is None:
                return
            if root.val not in to_delete and root.val is not None:
                if parent is None:
                    self.nodes = self.nodes + [root]
                    travel(root.left, root)
                    travel(root.right, root)
                else:
                    travel(root.left, parent)
                    travel(root.right, parent)
            else:
                travel(root.left, None)
                travel(root.right, None)
                root.val = 'null'
                root.left = None
                root.right = None

        travel(root, None)
        return self.nodes

libs = TreeLibs()
sol = Solution()
libs.printTree(sol.delNodes(libs.createBinaryTree([1,2,3,4,5,6,7]), [3, 5]))
#libs.printTree(sol.delNodes(libs.createBinaryTree([1,None,2,3,5,7,4,None,None,None,None,6]), [4]))