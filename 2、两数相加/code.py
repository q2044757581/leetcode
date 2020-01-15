class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        sum_val = l1.val + l2.val
        p = l3 = ListNode(int(sum_val % 10))
        left = int(sum_val / 10)
        l1 = l1.next
        l2 = l2.next
        while l1 and l2:
            sum_val = left + l1.val + l2.val
            l3.next = ListNode(int(sum_val % 10))
            left = int(sum_val / 10)
            l1 = l1.next
            l2 = l2.next
            l3 = l3.next
        while l1:
            sum_val = l1.val + left
            l3.next = ListNode(int(sum_val % 10))
            left = int(sum_val / 10)
            l1 = l1.next
            l3 = l3.next
        while l2:
            sum_val = l2.val + left
            l3.next = ListNode(int(sum_val % 10))
            left = int(sum_val / 10)
            l2 = l2.next
            l3 = l3.next
        if int(left) != 0:
            l3.next = ListNode(int(left))
        return p
