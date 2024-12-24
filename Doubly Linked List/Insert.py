class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.value)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def __str__(self):
        temp_node=self.head
        result=''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' <-> '
            temp_node = temp_node.next
        return result
        
    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        self.length+=1
    #Time complexity: O(1)
    #Space complexity: O(1)
    
    def prepend(self,value):
        new_node=Node(value)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        self.length+=1
    #Time complexity: O(1)
    #Space complexity: O(1)
    
    def traversal(self):
        current_node=self.head
        while current_node:
            print(current_node.value)
            current_node=current_node.next
    #Time complexity: O(n)
    #Space complexity: O(1)
    
    def rev_traversal(self):
        current_node=self.tail
        while current_node:
            print(current_node.value)
            current_node=current_node.prev
    #Time complexity: O(n)
    #Space complexity: O(1)
        
    def search(self,value):
        current_node=self.head
        index=0
        while current_node:
            if current_node.value==value:
                return index
            current_node=current_node.next
            index+=1
        return -1
    #Time complexity: O(n)
    #Space complexity: O(1)
    
    def get(self, index):
        if index<0 or index>=self.length:
            return None
        elif index<self.length//2:
            current_node= self.head
            for _ in range(index):
                current_node=current_node.next
        else:
            current_node= self.tail
            for _ in range(self.length-1,index,-1):
                current_node=current_node.prev
        return current_node
    #Time complexity: O(n)
    #Space complexity: O(1)
    
    def set_value(self,index, value):
        node=self.get(index)
        if node:
            node.value=value
            return True
        return False
    #Time complexity: O(n)
    #Space complexity: O(1)
    
    def insert(self,index,value):
        new_node=Node(value)
        if index<0 or index>self.length:
            print("Invalid index")
            return
        elif index==0:
            self.prepend(value)
            return True
        elif index==self.length:
            self.append(value)
            return True
        else:
            temp_node=self.get(index-1)
            new_node.next=temp_node.next
            new_node.prev=temp_node
            temp_node.next.prev=new_node
            temp_node.next=new_node
        self.length+=1
        
    #Time complexity: O(n)
    #Space complexity: O(1)
    
        
d_linked_list = DoublyLinkedList()
d_linked_list.append(10)
d_linked_list.append(20)
d_linked_list.append(30)
d_linked_list.prepend(5)
print(d_linked_list)
d_linked_list.insert(2,15)
print(d_linked_list)
d_linked_list.insert(0,2)
print(d_linked_list)