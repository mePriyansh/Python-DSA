import array

my_array1=array.array('i',[1,2,3,4,5])

def searchElement(array, value):
    for i in array:
        if i==value:
            return array.index(i)
    return "The element does not exist in the array"

print(searchElement(my_array1, 3))

#Time complexity: O(n)
#Space complexity: O(1)