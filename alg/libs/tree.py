class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class TreeLibs:
    def createBinaryTree(self, arr) -> TreeNode:
        def create(arr, x):
            if x >= len(arr) or arr[x] is None:
                return None
            node = TreeNode(arr[x])
            node.left = create(arr, 2*x + 1)
            node.right = create(arr, 2*x + 2)
            return node
        return create(arr, 0)

    def printTree(self, root):
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


