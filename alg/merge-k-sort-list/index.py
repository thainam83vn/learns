import sys
from libs.node import ListNode, NodeLib

class Solution:
    def done(self, lists: [ListNode]) -> bool:
        for l in lists:
            if l is not None:
                return False
        return True

    def pickMinIndex(self, lists: [ListNode]):
        minV = sys.maxsize
        minI = -1
        for i in range(len(lists)):
            l = lists[i]
            if l is not None and l.val < minV:
                minV = l.val
                minI = i
        return minI

    def mergeKLists(self, lists: [ListNode]) -> ListNode:
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]

        head = None
        pos = head

        while not self.done(lists):
            minI = self.pickMinIndex(lists)
            minV = lists[minI].val
            if head is None:
                head = ListNode(minV)
                pos = head
            else:
                pos.next = ListNode(minV)
                pos = pos.next
            lists[minI] = lists[minI].next
        return head


lib = NodeLib()
sol = Solution()
data = [
    lib.createList([1, 4, 5]),
    lib.createList([1, 3, 4]),
    lib.createList([2, 6])
]
lib.printListNode(sol.mergeKLists(data))