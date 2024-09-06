import array

my_array1=array.array('i',[1,2,3,4,5])
print(my_array1)
#Insert array (index, value)
my_array1.insert(0,6)
print(my_array1)

#Time Complexity: O(n)
#Space Complexity: O(1)