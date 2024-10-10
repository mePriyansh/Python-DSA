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

    def insert(self,index,value):
        new_node = Node(value)
        if index<0 or index>self.length:
            return False
        elif self.length ==0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
        return True
    
    
    def get(self,index):
        if index==-1:
            return self.tail
        elif index<-1 or index>=self.length:
            return None
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        return temp_node
    
        def pop_first(self):
            if self.head is None:
                return None
            popped_node = self.head
            if self.length == 1:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.length -= 1
            return popped_node
        
    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = self.tail= None
        else:
            temp=self.head
            while temp.next is not self.tail:
                temp=temp.next
            self.tail=temp
            temp.next=None
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        prev_node = self.get(index-1)
        if index>=self.length or index<-1:
            return None
        elif index==0:
            self.pop_first()
        elif index==self.length-1 or index == -1:
            self.pop()
        else:
            popped_node = prev_node.next
            prev_node.next = popped_node.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    #Time complexity: O(n)
    #Space complexity: O(1)
            
new_linked_list = LinkedList()
new_linked_list.prepend(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
print(new_linked_list)
new_linked_list.remove(1)
print(new_linked_list)

