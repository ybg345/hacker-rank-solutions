# Problem Link: https://www.hackerrank.com/challenges/30-linked-list/problem
# --------------------------------------------------------------------------


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self, head, data):
        new_node = Node(data)
    # If list is empty then; insert new node as the only element in the list
        if head is None:
            return new_node
    # For non empty list, we need to traverse to the end
        current = head
        while current.next != None:
            current = current.next 
        current.next = new_node
    # At end point (current.next becomes false) we set the new node as current.next value.
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 