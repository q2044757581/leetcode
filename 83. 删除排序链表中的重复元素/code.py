class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while p:
            if p.next:
                q = p.next
                if p.val == q.val:
                    # 重复， 进行删除
                    if q.next:
                        p.next = q.next
                    else:
                        p.next = None
                else:
                    p = p.next
            else:
                p = p.next
        return head