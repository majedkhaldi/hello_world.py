class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

def insertNodeAtTail(head, data):
    temp = Node(data)
    if head == None:
        head = temp
    else:
        curr=head 
        while  curr.next!=None:
                curr=curr.next
        curr.next=temp
    return head

head = insertNodeAtTail(None, 5)
head = insertNodeAtTail(head, 15)
