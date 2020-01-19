class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = 0
        p = 0

        while l1 and l2:
            if l1.val <= l2.val:
                if l3 == 0:
                    l3 = p = ListNode(l1.val)
                else:
                    l3.next = ListNode(l1.val)
                    l3 = l3.next
                l1 = l1.next
            else:
                if l3 == 0:
                    l3 = p = ListNode(l2.val)
                else:
                    l3.next = ListNode(l2.val)
                    l3 = l3.next
                l2 = l2.next
        while l1:
            if l3 == 0:
                l3 = p = ListNode(l1.val)
            else:
                l3.next = ListNode(l1.val)
                l3 = l3.next
            l1 = l1.next
        while l2:
            if l3 == 0:
                l3 = p = ListNode(l2.val)
            else:
                l3.next = ListNode(l2.val)
                l3 = l3.next
            l2 = l2.next
        return p

t = Solution()
print(t.mergeTwoLists(ListNode(2), ListNode(1)))