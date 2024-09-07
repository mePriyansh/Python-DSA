import numpy as np

two_d_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(two_d_array)

newArray = np.insert(two_d_array, 0, [[10, 11, 12]], axis=1)
print(newArray)

newArray1 = np.insert(two_d_array, 3, [[10, 11, 12]], axis=0)
print(newArray1)

newarray2=np.append(newArray1,[[13,14,15]],axis=0)
print(newarray2)

#Time Complexity: O(n*m)
#Space Complexity: O(n*m)