# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-5001,head)
        sorted_last = dummy #last node of the sorted portion

        while sorted_last and sorted_last.next: #to iterate until this reaches the endor serves like for i in range(len(list))
            prev = sorted_last
            curr = sorted_last.next
            min_node = curr
            min_prev = prev
            
            #find the minimum node and its preveous node
            while curr:
                if curr.val < min_node.val:

                    min_node = curr
                    min_prev = prev
                curr = curr.next
                prev = prev.next

            min_prev.next = min_node.next #remove the minimum element from its position
            min_node.next, sorted_last.next = sorted_last.next, min_node #add the min to the right place 
            
            sorted_last = sorted_last.next
            
        
        return dummy.next