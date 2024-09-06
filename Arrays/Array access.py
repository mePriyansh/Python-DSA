import array

my_array1=array.array('i',[1,2,3,4,5])

def accessElement(array, index):
    if index >= len(array):
        print("There is no element at this index")
    else:
        print(array[index])
        
accessElement(my_array1, 3)

#Time complexity: O(1)
#Space complexity: O(1)