class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        p = head
        # 先用一次遍历求长度
        while p:
            length += 1
            p = p.next
        del_index = length - n
        cnt = -1
        p = head
        if del_index == 0:
            if length == 1:
                head = None
            else:
                head = head.next
        else:
            while p:
                cnt += 1
                if cnt == del_index - 1:
                    if cnt != length - 2:
                        p.next = p.next.next
                    else:
                        p.next = None
                p = p.next
        return head

t = Solution()
result = t.removeNthFromEnd(ListNode(1), 1)
print(result)

