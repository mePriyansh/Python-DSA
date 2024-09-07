from array import *

#1. Create an array and traverse
arr_1 = array('i', [1, 2, 3, 4, 5])
for i in arr_1:
    print(i, end=" ")
    
#2. Access individual elements through indexes
print("\nAccess individual elements through indexes")
print(arr_1[3])

#3. Append any value to the array using append() method
print("\nAppend any value to the array using append() method")
arr_1.append(6)
print(arr_1)

#4. Insert value in an array using insert() method
print("\nInsert value in an array using insert() method")
arr_1.insert(8, 7)
print(arr_1)

#5. Extend the array using extend() method
print("\nExtend the array using extend() method")
arr_2=array('i', [8,9,10])
arr_1.extend(arr_2)
print(arr_1)

#6. Add items from list into array using fromlist() method
print("\nAdd items from list into array using fromlist() method")
tempList = [11, 12, 13] 
arr_1.fromlist(tempList)
print(arr_1)

#7. Remove any array element using remove() method
print("\nRemove any array element using remove() method")
arr_1.remove(13)
print(arr_1)

#8. Remove last array element using pop() method
print("\nRemove last array element using pop() method")
arr_1.pop()
print(arr_1)

#9. Fetch any element through its index using index() method
print("\nFetch any element through its index using index() method")
print(arr_1.index(7))

#10. Reverse a array using reverse() method
print("\nReverse a array using reverse() method")
arr_1.reverse()
print(arr_1)

#11. Get array buffer information through buffer_info() method
print("\nGet array buffer information through buffer_info() method")
print(arr_1.buffer_info())

#12. Check for number of occurrences of an element using count() method
print("\nCheck for number of occurrences of an element using count() method")
print(arr_1.count(7))

#13. Convert array to string using join() method as tostring() doesn't support array
print("\nConvert array to string using tostring()/join() method")
strTemp = ' '.join(map(str, arr_1))
print(strTemp)

#14. Slice Elements from an array
print("\nSlice Elements from an array")
print(arr_1[1:])
print(arr_1[1:4])
print(arr_1[:4])

#15. Convert array to a list using tolist() method
print("\nConvert array to a list using tolist() method")
list1=arr_1.tolist()
print(list1)

