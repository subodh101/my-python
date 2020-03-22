"""
https://practice.geeksforgeeks.org/problems/finding-middle-element-in-a-linked-list/1

"""

def findMid(head):
    # Code here
    if not head.next:
        return head
    def ll(head):
        i=1
        while(head.next):
            i+=1
            head=head.next
        return i
    h = head
    l=ll(h)
    a = l//2-1
    for i in range(a):
        head = head.next
    
    return head.next
