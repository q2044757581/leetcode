from typing import List


# 归并排序求解


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

    def mergeKLists(self, lists):
        if len(lists) == 0:
            return None
        # 判断k是奇偶
        list_copy = lists
        while True:
            k = len(list_copy)
            if k == 1:
                break
            l = []
            for i in range(int(k / 2)):
                # 两两归并
                l.append(self.mergeTwoLists(list_copy[i], list_copy[k - 1 - i]))
            if k % 2 == 1:
                l.append(list_copy[int(k / 2)])
            list_copy = l
        return list_copy[0]

l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)

t = Solution()
item = t.mergeKLists([l1, l2, l3])
temp = []
while item:
    temp.append(item.val)
    item = item.next
print(temp)