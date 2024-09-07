import numpy as np

two_d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_d_array)

def accessElement(array,  row, column):
    if row >= len(array) or column >= len(array[0]):
        print("Out of Bound")
    else:
        print(array[row][column])
    
accessElement(two_d_array, 1, 2)

#Time Complexity: O(1)
#Space Complexity: O(1)