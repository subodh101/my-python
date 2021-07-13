
# Logic

# While working with Linked List Always: create a head, keep updating it's next element and in the end return head.next.
# In this specific problem, create a new linked node and keep summing and forwarding the carry.
# Use python's direct check of None Attribute.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         carry = 0
#         head = ListNode()
#         n = head
#         flag = False
#         while(l1 or l2):
#             if flag:
#                 n.next = ListNode()
#                 n = n.next
#             flag = True
#             if l1 and l2:
#                 sum_ele = l1.val + l2.val + carry
#                 n.val = sum_ele % 10
#                 carry = sum_ele//10
#                 l1 = l1.next
#                 l2 = l2.next
#             elif l1:
#                 sum_ele = l1.val + carry
#                 n.val = sum_ele % 10
#                 carry = sum_ele//10
#                 l1 = l1.next
#             elif l2:
#                 sum_ele = l2.val + carry
#                 n.val = sum_ele % 10
#                 carry = sum_ele//10
#                 l2 = l2.next

#         if carry:
#             n.next = ListNode()
#             n = n.next
#             n.val = carry

#         return head


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        head = ListNode()
        n = head

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            sum_ele = v1 + v2 + carry
            n.next = ListNode(sum_ele % 10)
            n = n.next
            carry = sum_ele//10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next
