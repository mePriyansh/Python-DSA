class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
new_linked_list = LinkedList()
print("Initial Length: ",new_linked_list.length)
new_linked_list.append(10)
new_linked_list.append(20)
print("Head value of new node: ",new_linked_list.head.value)
print("Tail value of new node: ",new_linked_list.tail.value)
print("Length after adding two nodes: ",new_linked_list.length)