mylist = [1,2,33,4,5,6,7,8,9,10]
print(mylist)

#Update the list
mylist[2] = 3
print("\nUpdated List:")
print(mylist)

#Time Complexity: O(1)
#Space Complexity: O(1)

#Insertion
print("\nInsertion:")
print("New List")
mylist1 = [1,2,3,4,5,6,7,8,9,10]
print(mylist1)

#insert() method
mylist1.insert(0, 0)
print("\nInserted List:")
print(mylist1)

#Time Complexity: O(n)
#Space Complexity: O(1)

#append() method
print("\nappend() method:")
mylist1.append(11)
print("Appended List:")
print(mylist1)

#Time Complexity: O(1)
#Space Complexity: O(1)

newlist = [12,13,14]
#extend() method
print("\nextend() method:")
mylist1.extend(newlist)
print("Extended List:")
print(mylist1)

#Time Complexity: O(k) k is the number of elements in the list that is being added
#Space Complexity: O(k)

