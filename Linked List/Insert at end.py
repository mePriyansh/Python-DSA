class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        temp_node=self.head
        result=' '
        while temp_node is not None:
            result+=str(temp_node.value)
            if temp_node.next is not None:
                result+='->'
            temp_node=temp_node.next
        return result

#Insertion at the end of the linked list
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
#Time complexity: O(1)
#Space complexity: O(1)
        
#Insertion at the beginning of the linked list
    def prepend(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
#Time complexity: O(1)
#Space complexity: O(1)
        
        
new_linked_list = LinkedList()
print("Initial Length: ",new_linked_list.length)
new_linked_list.append(10)
new_linked_list.append(20)
print("Linked list after appending",new_linked_list)
new_linked_list.prepend(5)
print("Linked list after prepending",new_linked_list)