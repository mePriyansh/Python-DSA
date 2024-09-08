my_list=['a','b','c','d','e','f','g','h']
print(my_list)

#Slicing the list
print("Slicing list")
print(my_list[1:3])
print(my_list[:4])
print(my_list[2:])

#Updating the list using slicing
print("Updating list using slicing")
my_list[0:2] = ['x','y']
print(my_list)

#Deleting the list
print("Deleting list using pop")
print(my_list.pop(1))               
print(my_list)

#Time complexity: O(n)/O(1) - pop() is O(1) and pop(0) is O(n)
#Space complexity: O(1)

#Deleting the list using delete
print("Deleting list using delete")
del my_list[0:2]
print(my_list)

#Time complexity: O(n)
#Space complexity: O(1)

#Deleting the list using remove
print("Deleting list using remove")
my_list.remove('h')
print(my_list)

#Time complexity: O(n)
#Space complexity: O(1)