class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        lenghtOfLL = 0
        auxLL = head
        
        while auxLL != None:
            lenghtOfLL += 1
            auxLL = auxLL.next
        auxLL = head
        for index in range((lenghtOfLL//2)):
            auxLL = auxLL.next
        
        return auxLL
            
