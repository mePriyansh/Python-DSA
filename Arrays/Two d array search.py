import numpy as np

two_d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_d_array)

def searchArray(array, target):
    for i in range(len(array)):                                     #O(m*n)
        for j in range(len(array[i])):                              #O(n)                         
            if array[i][j] == target:
                return "Target found at index: " + str(i) + ", " + str(j)
    return "Target not found"

print(searchArray(two_d_array, 5))
print(searchArray(two_d_array, 11))

#Time complexity: O(n^2)/O(m*n)
#Space complexity: O(1)