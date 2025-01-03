class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)
    #Time complexity: O(1)
    #Space complexity: O(1)

class DoublyLinkedList:
    #No elements in the list
    # def __init__(self):
    #     self.head = None
    #     self.tail = None
    #     self.length = 0
    
    #One element in the list
    def __init__(self,value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
    #Time complexity: O(1)
    #Space complexity: O(1)
    
    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' <-> '
            temp_node = temp_node.next
        return result
        
d_linked_list = DoublyLinkedList(10)
print(d_linked_list.head.value)