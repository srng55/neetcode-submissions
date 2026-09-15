# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy=ListNode(0,head)
        group_before=dummy

        while True:

            group_end=self.getKth(group_before,k)

            if not group_end:
                break

            next_group=group_end.next

            #reverse

            prev=next_group
            curr=group_before.next

            while curr != next_group:
                tmp=curr.next
                curr.next=prev
                prev=curr
                curr=tmp

            tmp=group_before.next
            group_before.next=group_end
            group_before=tmp

        return dummy.next

    def getKth(self, node, k):

        while node and k > 0:
            node = node.next
            k -= 1

        return node

