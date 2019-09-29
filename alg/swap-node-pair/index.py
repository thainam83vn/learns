from libs.node import ListNode, NodeLib

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        next = head.next
        temp = next.next
        next.next = head
        head.next = self.swapPairs(temp)
        return next

libs = NodeLib()
sol = Solution()
libs.printListNode(sol.swapPairs(libs.createList([1, 2, 3, 4])))