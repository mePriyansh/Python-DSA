import numpy as np

two_d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_d_array)

def Traversal(array):
    for i in range(len(array)):                                     #O(m*n)
        for j in range(len(array[i])):                              #O(n)                         
            print(array[i][j])
            
Traversal(two_d_array)            

#Time complexity: O(n^2)
#Space complexity: O(1)