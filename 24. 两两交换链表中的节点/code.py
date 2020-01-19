class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        # 每两个换下顺序
        p = result = head
        cnt = 0
        while p:
            if cnt == 0:
                if p.next:
                    q = p.next
                else:
                    break
                if q.next:
                    p.next = q.next
                else:
                    p.next = None
                result = q
                q.next = p
                cnt += 1
            else:
                # 可以进行一次交换
                if p.next:
                    if p.next.next:
                        if p.next.next.next:
                            l1 = p.next
                            l2 = p.next.next
                            l3 = p.next.next.next
                            p.next = l2
                            l2.next = l1
                            l1.next = l3
                            p = l1
                        else:
                            l1 = p.next
                            l2 = p.next.next
                            p.next = l2
                            l2.next = l1
                            l1.next = None
                            p = l1
                    else:
                        p = p.next
                else:
                    p = p.next
        return result

# [1,2,3,4]
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
# l1.next.next.next = ListNode(4)
# l1.next.next.next.next = ListNode(5)

t = Solution()
item = t.swapPairs(l1)
temp = []
while item:
    temp.append(item.val)
    item = item.next
print(temp)
