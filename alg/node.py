# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class NodeLib:
    def createList(self, arr) -> ListNode:
        if len(arr) == 0:
            return None
        node = ListNode(arr[0])
        node.next = self.createList(arr[1:])
        return node

    def printListNode(self, root):
        if root is None:
            return
        print(root.val, ' -> ', end='')
        self.printListNode(root.next)