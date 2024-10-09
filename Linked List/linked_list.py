class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

#Time Complexity: O(1)
#Space Complexity: O(1)

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
        
new_linked_list = LinkedList(10)
print(new_linked_list.head.value)

#Time Complexity: O(1)
#Space Complexity: O(1)
        
#Empty Linked List
# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
# ll=LinkedList()
# print(ll.length)        

#Time Complexity: O(1)
#Space Complexity: O(1)